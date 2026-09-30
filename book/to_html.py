"""Convert the study book (LaTeX with a small, fixed macro set) into one HTML page.

Usage: python to_html.py   ->  ../index.html
Math is kept as TeX and rendered in the browser by KaTeX.
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "study_book.tex")
OUT = os.path.join(HERE, os.pardir, "index.html")
B = "\\"

# ---------------------------------------------------------------- helpers
def group(s, i):
    """s[i] == '{' -> (content, index after the closing brace)."""
    assert s[i] == "{", s[i:i + 30]
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == B:
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces near " + s[i:i + 60])


def opt(s, i):
    """optional [..] argument at i -> (content or None, new index)."""
    if i < len(s) and s[i] == "[":
        j = s.index("]", i)
        return s[i + 1:j], j + 1
    return None, i


def apply_cmd(s, name, fn, nargs=1, optional=False):
    out, i, pat = [], 0, re.compile(re.escape(B + name) + r"(?![A-Za-z])")
    while True:
        m = pat.search(s, i)
        if not m:
            out.append(s[i:])
            return "".join(out)
        out.append(s[i:m.start()])
        j = m.end()
        o = None
        if optional:
            while j < len(s) and s[j] == " ":
                j += 1
            o, j = opt(s, j)
        args = []
        for _ in range(nargs):
            while j < len(s) and s[j] in " \n":
                j += 1
            a, j = group(s, j)
            args.append(a)
        out.append(fn(*args, o) if optional else fn(*args))
        i = j


# ---------------------------------------------------------------- math protection
MATH = []


def protect(s):
    def keep(m):
        MATH.append(m.group(0))
        return f"\x00M{len(MATH) - 1}\x00"
    s = re.sub(r"\\\[.*?\\\]", keep, s, flags=re.S)
    s = re.sub(r"(?<!\\)\$[^$]+?(?<!\\)\$", keep, s, flags=re.S)
    return s


def restore(s):
    return re.sub(r"\x00M(\d+)\x00", lambda m: html.escape(MATH[int(m.group(1))], quote=False), s)


# ---------------------------------------------------------------- environments
def table(body, spec_cols=None):
    body = re.sub(r"\\(toprule|midrule|bottomrule)", "", body)
    rows = [r.strip() for r in re.split(r"\\\\", body) if r.strip()]
    out = ["<div class='tbl'><table>"]
    for k, r in enumerate(rows):
        cells = [c.strip() for c in re.split(r"(?<!\\)&", r)]
        tag = "th" if k == 0 and ("Question" in r or "Say it" in r) else "td"
        out.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in cells) + "</tr>")
    out.append("</table></div>")
    return "".join(out)


def envs(s):
    # tables first (they contain & and \\)
    s = re.sub(r"\\begin\{tabularx\}\{[^}]*\}\{(?:[^{}]|\{[^{}]*\})*\}(.*?)\\end\{tabularx\}",
               lambda m: table(m.group(1)), s, flags=re.S)
    s = re.sub(r"\\begin\{tabular\}\{[^}]*\}(.*?)\\end\{tabular\}", lambda m: table(m.group(1)), s, flags=re.S)
    s = re.sub(r"\\begin\{center\}(.*?)\\end\{center\}", r"\1", s, flags=re.S)

    def lists(s, env, tag):
        pat = re.compile(r"\\begin\{" + env + r"\}(.*?)\\end\{" + env + r"\}", re.S)
        while pat.search(s):
            s = pat.sub(lambda m: f"<{tag}>" + "".join(
                f"<li>{it.strip()}</li>" for it in re.split(r"\\item\b", m.group(1)) if it.strip()) + f"</{tag}>", s)
        return s
    s = lists(s, "itemize", "ul")
    s = lists(s, "enumerate", "ol")

    s = re.sub(r"\\begin\{summary\}\{(.*?)\}", r"<div class='card sum'><div class='ttl'>2-minute summary · \1</div><div class='bd'>", s)
    s = s.replace(B + "end{summary}", "</div></div>")
    s = re.sub(r"\\begin\{chain\}\{(.*?)\}", r"<div class='card chain'><div class='ttl'>\1</div><div class='bd'>", s)
    s = s.replace(B + "end{chain}", "</div></div>")

    counter = {"n": 0}

    def qa(m):
        counter["n"] += 1
        who, title = m.group(1) or "", m.group(2)
        kind = 'a' if 'asked' in title else 'e' if 'cexam' in title else 'p'
        return (f"<details class='card qa k-{kind}' open><summary class='ttl'><span>Q · {title}</span>"
                f"<span class='who'>{who}</span></summary><div class='bd'>")
    s = re.sub(r"\\begin\{qabox\}(?:\[(.*?)\])?\{(.*?)\}\s*\n", qa, s)
    s = s.replace(B + "end{qabox}", "</div></details>")
    return s


# ---------------------------------------------------------------- inline commands
def inline(s):
    s = re.sub(r"\\(newcommand|renewcommand)\{\\\w+\}(\[\d\])?\{.*\}\s*\n", "", s)
    s = re.sub(r"\\newtcolorbox\{.*?\n\s*left=.*?\}\s*\n", "", s, flags=re.S)
    s = apply_cmd(s, "pic", lambda a: f"<div class='pic'><b>Picture it.</b> {a}</div>")
    s = apply_cmd(s, "board", lambda a: f"<div class='board'><b>Board drill</b> (write it by hand 3 times). {a}</div>")
    s = apply_cmd(s, "hook", lambda a: f"<p class='hook'>→ <b>hook:</b> <i>{a}</i></p>")
    s = apply_cmd(s, "cq", lambda a: f"<p class='cq'><b>Q.</b> {a}</p>")
    s = apply_cmd(s, "ca", lambda a: f"<p class='ca'><b>A.</b> {a}</p>")
    s = apply_cmd(s, "from", lambda a: f"<p class='from'><b>From:</b> {a}</p>")
    s = re.sub(r"\\asked\s*", "<span class='badge b-a'>ASKED BEFORE</span> ", s)
    s = re.sub(r"\\cexam\s*", "<span class='badge b-e'>COURSE EXAM</span> ", s)
    s = re.sub(r"\\pred\s*", "<span class='badge b-p'>PREDICTED</span> ", s)
    s = apply_cmd(s, "src", lambda a: f"<p class='src'>Source: {a}</p>")
    s = re.sub(r"\\ans\b\\?\s*", "<p><b class='lbl'>Say:</b> ", s)
    s = re.sub(r"\\formula\b", "<p><b class='lbl'>Write:</b> ", s)
    s = re.sub(r"\\follow\b\\?\s*", "<p><b class='lbl'>Follow-up:</b> ", s)
    for c, t in (("textsf", "b"), ("textbf", "b"), ("emph", "i"), ("texttt", "code")):
        s = apply_cmd(s, c, lambda a, t=t: f"<{t}>{a}</{t}>")
    s = re.sub(r"\\color\{[^}]*\}", "", s)
    s = re.sub(r"\\(medskip|smallskip|bigskip|hfill|clearpage|footnotesize|small|noindent|par)\b", " ", s)
    s = s.replace(B + "textbullet{}", "•").replace(B + "textbullet", "•")
    s = s.replace("``", "“").replace("''", "”").replace("---", "—").replace("--", "–")
    s = s.replace(B + "&", "&amp;").replace(B + "%", "%").replace(B + "\\", "<br>")
    s = s.replace(B + "\n", " ").replace(B + " ", " ").replace("~", "&nbsp;").replace(B + "'", "")
    s = re.sub(r"\\q?quad\b", "&emsp;", s).replace(B + "_", "_")
    s = re.sub(r'\\"([aou])', lambda m: {"a": "ä", "o": "ö", "u": "ü"}[m.group(1)], s)
    s = s.replace(B + "'e", "é")
    return s


def sections(s):
    toc = []

    def sec(m):
        level = 2 if m.group(1) else 1
        title = m.group(3)
        sid = "s" + str(len(toc))
        toc.append((level, title, sid))
        tag = "h2" if level == 1 else "h3"
        return f"<{tag} id='{sid}'>{title}</{tag}>"
    s = re.sub(r"\\(sub)?section(\*?)\{(.*?)\}", sec, s)
    return s, toc


def paragraphs(s):
    parts = re.split(r"\n\s*\n", s)
    return "\n".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in parts if p.strip())


# ---------------------------------------------------------------- build
main = open(MAIN, encoding="utf-8").read()
files = re.findall(r"\\input\{(\w+)\}", main.split(B + "begin{document}")[1])
body = ""
for f in files:
    t = open(os.path.join(HERE, f + ".tex"), encoding="utf-8").read()
    t = re.sub(r"(?<!\\)%.*", "", t)
    body += "\n\n" + t
body = protect(body)
body = envs(body)
body = inline(body)
body, toc = sections(body)
body = paragraphs(body)
body = restore(body)

nav = "".join(f"<a class='l{lv}' href='#{sid}'>{restore(inline(protect(t)))}</a>" for lv, t, sid in toc)
page = open(os.path.join(HERE, "page_template.html"), encoding="utf-8").read()
page = page.replace("{{NAV}}", nav).replace("{{BODY}}", body)
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page) // 1024, "KB,", len(toc), "sections")

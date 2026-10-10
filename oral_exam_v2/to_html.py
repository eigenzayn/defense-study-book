"""Turn the oral-exam book (LaTeX) into one static web page with MathJax.

    python to_html.py  ->  index.html next to this script
The page shows every question with its origin label, a filter (all / asked before / predicted),
a search box and a practice mode in which only the question and the core sentence are shown.
"""
import html, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = [("partA_thesis.tex", "A", "Thesis"), ("partB_mlp.tex", "B", "Machine Learning and Perception"),
         ("partC_aisim.tex", "C", "AI for Simulation (rCFD)")]


def braced(s, i):
    """Return (content, end) of the {...} group that starts at s[i] == '{'."""
    assert s[i] == "{", s[i:i + 30]
    d = 0
    for j in range(i, len(s)):
        if s[j] == "{" and s[j - 1] != "\\":
            d += 1
        elif s[j] == "}" and s[j - 1] != "\\":
            d -= 1
            if d == 0:
                return s[i + 1:j], j + 1
    raise ValueError("unbalanced braces")


def text(t):
    """LaTeX text (outside maths) to HTML; maths is kept for MathJax."""
    out, i = [], 0
    while i < len(t):
        if t[i] == "$":
            j = t.index("$", i + 1)
            out.append(html.escape(t[i:j + 1], quote=False))
            i = j + 1
            continue
        k = t.find("$", i)
        chunk = t[i:] if k < 0 else t[i:k]
        out.append(prose(chunk))
        i = len(t) if k < 0 else k
    return "".join(out)


def prose(c):
    c = html.escape(c, quote=False)
    c = re.sub(r"\\(emph|textit)\{([^{}]*)\}", r"<em>\2</em>", c)
    c = re.sub(r"\\(textsf|textbf)\{([^{}]*)\}", r"<strong>\2</strong>", c)
    c = re.sub(r"\\texttt\{([^{}]*)\}", r"<code>\1</code>", c)
    c = re.sub(r"\\(cite[pt]?)\{[^{}]*\}", "", c)
    rep = [("``", "&ldquo;"), ("''", "&rdquo;"), ("---", "&mdash;"), ("--", "&ndash;"),
           ("~", "&nbsp;"), ("\\,", "&thinsp;"), ("\\ldots", "&hellip;"), ("\\&", "&amp;"),
           ("\\%", "%"), ("\\_", "_"), ("\\ ", " "), ("\\'e", "é"), ("\\\"o", "ö"),
           ("\\'{e}", "é"), ("\\\"{o}", "ö"), ("\\textbullet{}", "&bull;"), ("\\par", "")]
    for a, b in rep:
        c = c.replace(a, b)
    c = re.sub(r"\\(color\{[^{}]*\}|small|footnotesize|sffamily|noindent|smallskip)", "", c)
    return c


def maths_block(env, body):
    return '<div class="math">\\[\\begin{%s}%s\\end{%s}\\]</div>' % (env, html.escape(body, quote=False), env)


def body_html(b):
    """Convert the inside of one qabox."""
    parts, i = [], 0
    pat = re.compile(r"\\(origin|core|nums|summary|src)\{|\\explain|\\derive|\\begin\{(align\*|equation\*|gather\*)\}"
                     r"|\\begin\{itemize\}|\\\[")
    buf = ""
    while True:
        m = pat.search(b, i)
        if not m:
            buf += b[i:]
            break
        buf += b[i:m.start()]
        if buf.strip():
            parts.append(("p", buf)); buf = ""
        tok = m.group(0)
        if tok.startswith("\\origin"):
            kind, e = braced(b, m.end() - 1)
            note, e = braced(b, e)
            parts.append(("origin", (kind, note))); i = e
        elif m.group(1) in ("core", "nums", "summary", "src"):
            c, e = braced(b, m.end() - 1)
            parts.append((m.group(1), c)); i = e
        elif tok == "\\explain":
            parts.append(("explain", None)); i = m.end()
        elif tok == "\\derive":
            parts.append(("derive", None)); i = m.end()
        elif tok.startswith("\\begin{itemize}"):
            e = b.index("\\end{itemize}", m.end())
            items = [x.strip() for x in b[m.end():e].split("\\item") if x.strip()]
            parts.append(("list", items)); i = e + len("\\end{itemize}")
        elif tok == "\\[":
            e = b.index("\\]", m.end())
            parts.append(("display", b[m.end():e])); i = e + 2
        else:
            env = m.group(2)
            end = "\\end{%s}" % env
            e = b.index(end, m.end())
            parts.append(("math", (env, b[m.end():e]))); i = e + len(end)
    if buf.strip():
        parts.append(("p", buf))

    origin, core, rest = None, "", []
    pending = None
    for kind, val in parts:
        if kind == "origin":
            origin = val
        elif kind == "core":
            core = text(val)
        elif kind == "explain":
            pending = "Explain"
        elif kind == "derive":
            rest.append('<div class="lab">Derivation</div>')
        elif kind == "p":
            lab = '<span class="lab">%s.</span> ' % pending if pending else ""
            pending = None
            rest.append("<p>%s%s</p>" % (lab, text(val.strip())))
        elif kind == "nums":
            rest.append('<p><span class="lab">Numbers.</span> %s</p>' % text(val))
        elif kind == "math":
            rest.append(maths_block(*val))
        elif kind == "display":
            rest.append('<div class="math">\\[%s\\]</div>' % html.escape(val, quote=False))
        elif kind == "list":
            rest.append("<ul>%s</ul>" % "".join("<li>%s</li>" % text(x) for x in val))
        elif kind == "summary":
            rest.append('<p class="summary"><span>Summary:</span> %s</p>' % text(val))
        elif kind == "src":
            rest.append('<p class="src">Source: %s</p>' % text(val))
    return origin, core, "\n".join(rest)


def table_html(t):
    rows = [r.strip() for r in re.split(r"\\\\", t) if r.strip()]
    out = []
    for r in rows:
        r = re.sub(r"\\(toprule|midrule|bottomrule)", "", r).strip()
        if not r:
            continue
        out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % text(c.strip()) for c in r.split("&")))
    return '<table class="talk">%s</table>' % "".join(out)


def part_html(fname, letter, title):
    s = open(os.path.join(HERE, fname), encoding="utf8").read()
    s = re.sub(r"(?m)^%.*$", "", s)
    s = re.sub(r"\\section\{[^\n]*\}\n", "", s, count=1)
    secs, toc, qn = [], [], 0
    pos = 0
    pat = re.compile(r"\\subsection\{([^\n]*)\}|\\begin\{qabox\}\{|\\begin\{tipbox\}|\\begin\{tabularx\}")
    intro_done = False
    while True:
        m = pat.search(s, pos)
        chunk = s[pos:m.start()] if m else s[pos:]
        chunk = re.sub(r"\\(begin|end)\{center\}", "", chunk).strip()
        if chunk:
            secs.append('<p class="intro">%s</p>' % text(chunk))
        if not m:
            break
        tok = m.group(0)
        if tok.startswith("\\subsection"):
            sid = "%s-%d" % (letter, len(toc) + 1)
            toc.append((sid, m.group(1)))
            secs.append('<h3 id="%s">%s</h3>' % (sid, text(m.group(1))))
            pos = m.end()
        elif tok.startswith("\\begin{qabox}"):
            qtitle, e = braced(s, m.end() - 1)
            end = s.index("\\end{qabox}", e)
            origin, core, rest = body_html(s[e:end])
            qn += 1
            kind, note = origin or ("predicted", "")
            badge = "ASKED BEFORE" if kind == "asked" else "PREDICTED"
            secs.append(
                '<details class="qa %s" open data-text="%s"><summary><span class="qid">%s%d</span> %s'
                '<span class="badge %s">%s</span></summary>'
                '<p class="origin">%s</p><p class="core"><span class="lab">Core.</span> %s</p>'
                '<div class="rest">%s</div></details>'
                % (kind, html.escape(re.sub(r"[\\${}]", "", qtitle + " " + note)).lower(), letter, qn,
                   text(qtitle), kind, badge, text(note), core, rest))
            pos = end + len("\\end{qabox}")
        elif tok.startswith("\\begin{tipbox}"):
            end = s.index("\\end{tipbox}", m.end())
            secs.append('<div class="tip">%s</div>' % text(s[m.end():end].strip()))
            pos = end + len("\\end{tipbox}")
        else:
            _, k = braced(s, m.end())          # width
            _, k = braced(s, k)                # column specification
            end = s.index("\\end{tabularx}", k)
            secs.append(table_html(s[k:end]))
            pos = end + len("\\end{tabularx}")
    return toc, "\n".join(secs), qn


blocks, nav = [], []
for f, letter, title in PARTS:
    toc, body, n = part_html(f, letter, title)
    nav.append('<li><a href="#part-%s">%s. %s</a> <span class="n">(%d)</span><ul>%s</ul></li>'
               % (letter, letter, html.escape(title), n,
                  "".join('<li><a href="#%s">%s</a></li>' % (i, text(t)) for i, t in toc)))
    blocks.append('<section id="part-%s"><h2>%s. %s</h2>%s</section>' % (letter, letter, html.escape(title), body))

page = open(os.path.join(HERE, "page_template.html"), encoding="utf8").read()
page = page.replace("{{NAV}}", "\n".join(nav)).replace("{{BODY}}", "\n".join(blocks))
open(os.path.join(HERE, "index.html"), "w", encoding="utf8").write(page)
print("index.html written,", sum(len(b) for b in blocks) // 1000, "kB of content")

"""Insert a priority badge at the start of every qabox title (idempotent).
A = asked in a past defense, E = course exam, P = predicted."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TAGS = {
    "s1_erm": "AAAAE",
    "s2_backprop": "AAAAA",
    "s3_training": "AAAAPAP",
    "s4_lstm": "EEEEEEEAEP",
    "s5_attention": "AAAA",
    "s6_classic": "AAAAAA",
    "s7_rcfd": "PPPPPP",
    "s8_predicted": "AAPP",
    "s10_hot": "PPPPPPPPPPP",
    "s11_mlat": "EEEEEEEEEEEEE",
}
MAC = {"A": "\\asked ", "E": "\\cexam ", "P": "\\pred "}
pat = re.compile(r"(\\begin\{qabox\}(?:\[[^\]]*\])?\{)(\\(?:asked|cexam|pred) )?")
for f, tags in TAGS.items():
    p = os.path.join(HERE, f + ".tex")
    s = open(p, encoding="utf-8").read()
    n = len(pat.findall(s))
    assert n == len(tags), (f, n, len(tags))
    it = iter(tags)
    s = pat.sub(lambda m: m.group(1) + MAC[next(it)], s)
    open(p, "w", encoding="utf-8").write(s)
    print(f, n, tags.count("A"), tags.count("E"), tags.count("P"))

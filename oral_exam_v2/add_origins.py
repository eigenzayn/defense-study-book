"""Add an origin label to every question: asked before (with examiner, from the list of past
defenses in 'Msc. AI Defense Questions.xlsx') or predicted (with the basis of the prediction).

    python add_origins.py      (idempotent: existing \\origin lines are replaced)
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))

# key: start of the question title  ->  (kind, note)
A = "asked"
P = "predicted"
ORIGIN = {
 # Part A, thesis
 "What problem did you solve": (A, "thesis part, committee Küng/Klambauer: ``What problem was solved?''"),
 "Why should anybody care": (A, "thesis part, Mara (``What benefit does your thesis bring to the world?'') and Küng (``why should I care?'')"),
 "What is future work": (A, "thesis part, Küng committee (``What would you do differently?''), Mara (``How could I extend my work?'')"),
 "Which papers influenced you most": (A, "thesis part, Mara (``Which was the paper your thesis was most influenced by?'')"),
 "Why is this AI": (A, "thesis part, Küng committee (``Why and how does ML solve this problem?'')"),
 "How do you know your results are correct": (A, "thesis part, Ulrich (``statistical methods employed, why other methods were not chosen'')"),
 # Part B, ML and Perception
 "Write down a supervised data set": (A, "Klambauer (several students), Berger-Weber committee"),
 "What is the generalization error": (A, "Klambauer (Fürnkranz committee), Schedl committee"),
 "What is a loss function": (A, "Klambauer, March 2026 (``not all losses are differentiable, 0--1 loss'')"),
 "Show ERM on linear regression": (A, "Klambauer (Küng committee), Schedl committee"),
 "Overfitting, underfitting": (P, "DLNN script Sec.~5.4; bias and MSE were asked only in signal processing (Huemer)"),
 "Write the formula of a neuron": (A, "Schlüter"),
 "A deep network with and without": (A, "Schlüter"),
 "Universal function approximation": (A, "Lehner"),
 "Explain backpropagation": (A, "Hochreiter, Klambauer, Kofler (several students)"),
 "Write the recursive formula": (A, "Klambauer, Kofler (``delta error of the $l$-th layer'')"),
 "What is the delta at the output": (A, "Hochreiter (softmax + cross-entropy)"),
 "Vanishing and exploding gradients": (A, "Schedl committee (``backpropagation, vanishing gradients'')"),
 "Write gradient descent": (A, "Schlüter, Klambauer"),
 "Which optimizers do you know": (A, "Hochreiter"),
 "Are there training methods other": (A, "Klambauer"),
 "Which activation functions": (A, "Hochreiter (``which one is from Linz?'')"),
 "Which regularization techniques": (A, "Hochreiter"),
 "Why does initialization matter": (P, "DLNN script Ch.~9--10"),
 "What is a CNN": (P, "DLNN script Ch.~6"),
 "ResNet, and U-Net": (A, "U-Net asked by Klambauer in Life Science; ResNet predicted from the SS25 script"),
 "Explain the forward pass of a recurrent": (A, "J.~Küng committee, Lehner (``main idea of RNNs'')"),
 "Why do plain RNNs fail": (P, "LSTM lecture (Hochreiter); vanishing gradients were asked"),
 "Bidirectional RNNs": (A, "Schlüter (``RNN from the future'')"),
 "Explain attention and the Transformer": (A, "Rekabsaz, Lehner, Klambauer (self-attention matrices)"),
 "Transformers are permutation": (A, "Lehner"),
 "Compare RNN and Transformer": (A, "Lehner ($O(N)$ against $O(N^2)$)"),
 "Explain the support vector machine": (A, "Kofler, March 2026 committee"),
 "What is a kernel": (A, "Kofler"),
 "What is the VC dimension": (A, "Kofler"),
 "Likelihood, maximum likelihood": (A, "Widmer (several students)"),
 "Derive the REINFORCE loss": (A, "Hochreiter"),
 "How do you evaluate a classifier": (A, "R.~Küng committee (AUC), Mara committee (confusion matrix)"),
 "How else can you measure robustness": (A, "Klambauer"),
}
DEFAULT = {
 "partA_thesis.tex": (P, "your thesis: everything you used can be asked"),
 "partC_aisim.tex": (P, "no past questions from Prof.~Pirker yet; predicted from his lecture and the thesis figures"),
}

for f in ("partA_thesis.tex", "partB_mlp.tex", "partC_aisim.tex"):
    p = os.path.join(HERE, f)
    s = open(p, encoding="utf8").read()
    s = re.sub(r"\n\\origin\{[^\n]*\}\{[^\n]*\}(?=\n)", "", s)
    out, n = [], 0
    for line in s.split("\n"):
        out.append(line)
        m = re.match(r"\\begin\{qabox\}\{(.*)\}\s*$", line)
        if m:
            title = m.group(1)
            hit = [v for k, v in ORIGIN.items() if title.startswith(k)]
            kind, note = hit[0] if hit else DEFAULT.get(f, (P, "predicted"))
            out.append("\\origin{%s}{%s}" % (kind, note))
            n += 1
    open(p, "w", encoding="utf8").write("\n".join(out))
    print(f, n, "questions labelled")

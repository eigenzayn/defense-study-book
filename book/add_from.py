"""Insert a \\from{course · chapter · origin} line after every qabox title (idempotent)."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PD = "asked in past defenses"
DL1 = "DL Basic Techniques (DLNN I)"
LSTM = "LSTM \\& Transformers (Hochreiter)"
MLS = "ML: Supervised Techniques"
NM = "Numerical Methods in Fluid Mechanics (Pirker)"
MLAT = "ML: Advanced Techniques"
FROM = {
    "s1_erm": [
        f"{DL1} · Ch.~3 Notation, Ch.~5.1 ERM · {PD}",
        f"{DL1} · Ch.~5.2--5.3 Generalization error · {PD}",
        f"{DL1} · Ch.~4.1 Loss functions · {PD}",
        f"{DL1} · Ch.~4.1 Linear model · {PD}",
        f"{DL1} · Ch.~5.4 Model complexity; Geometric DL exam map",
    ],
    "s2_backprop": [
        f"{DL1} · Ch.~4.6 Backpropagation · {PD}",
        f"{DL1} · Ch.~4.6--4.7 Delta recursion · {PD}",
        f"{DL1} · Table~4.1 Output deltas · {PD}",
        f"{DL1} · Ch.~4.7 Vanishing gradients · {PD}",
        f"{DL1} · Ch.~3--4 Neuron, MLP · {PD}",
    ],
    "s3_training": [
        f"{DL1} · Ch.~10.4 Self-normalization, Ch.~11 Activations · {PD}",
        f"{DL1} · Ch.~7 Optimizers · {PD}",
        f"{DL1} · Ch.~8 Regularization · {PD}",
        f"{MLS} · feature selection · {PD}",
        f"{DL1} · Ch.~9 Initialization · predicted",
        f"{MLS} (Lehner) unit~6; DLNN~II theory chapter · {PD}",
        f"{DL1} · Ch.~6 CNNs; DL Architectures (DLNN II) · ResNet · predicted",
    ],
    "s4_lstm": [
        f"{LSTM} · RNN architectures (Jordan, Elman, NARX, TDNN) · course exam",
        f"{LSTM} · BPTT, truncated BPTT, RTRL · course exam",
        f"{LSTM} · vanishing gradient in time · course exam",
        f"{LSTM} · LSTM cell, constant error carousel · course exam",
        f"{LSTM} · forget gate, drift, ticker steps · course exam",
        f"{LSTM} · LSTM variants, GRU · course exam",
        f"{LSTM} · LSTM dropout, zoneout · course exam",
        f"{LSTM} · bidirectional RNN, sequence classification · {PD}",
        f"{LSTM} · xLSTM (sLSTM, mLSTM) · course exam",
        "IML research · modern Hopfield networks (Ramsauer et al.~2020) · predicted",
    ],
    "s5_attention": [
        f"{LSTM} · Transformer; NLP course · {PD}",
        f"{LSTM} · scaled dot-product attention · {PD}",
        f"{MLS} (Lehner) unit~7; {LSTM} · {PD}",
        f"{MLS} (Lehner) unit~7; {LSTM} · {PD}",
    ],
    "s6_classic": [
        f"{MLS} · SVM · {PD}",
        f"{MLS} · kernels · {PD}",
        f"{MLS}; statistical learning theory · {PD}",
        "Probabilistic Models (Widmer); ML: Unsupervised Techniques · " + PD,
        "Deep Reinforcement Learning · policy gradient · " + PD,
        f"{MLS}; AI and Visualization · evaluation · {PD}",
    ],
    "s7_rcfd": [
        f"{NM} · rCFD lecture, slides 16--34 · predicted",
        f"{NM} · rCFD slides 50--51; thesis Sec.~2.4 · predicted",
        f"Thesis Sec.~2.8.1; {NM} · explicit limits · predicted",
        f"{NM} · FV~II numerical diffusion; thesis Sec.~4.2 · predicted",
        f"{NM} · rCFD slides 59--72 digital twins · predicted",
        f"{NM} · GovEq, FV, SIMPLE, turbulence · predicted",
    ],
    "s8_predicted": [
        f"Thesis, Appendix A1 (story summary) · {PD}",
        f"Thesis, Ch.~8 and future work · {PD}",
        "Thesis $\\times$ DL: graph neural networks · predicted",
        f"Thesis $\\times$ {LSTM} · predicted",
    ],
    "s10_hot": [
        "IML research overview · predicted",
        "NeuralDEM (Alkin, Brandstetter, Pirker et al.~2024) · predicted",
        f"xLSTM (Beck et al.~2024); {LSTM} · predicted",
        "RUDDER (Arjona-Medina et al.~2019); Deep RL · predicted",
        "FID (Heusel et al.~2017) · predicted",
        f"{MLAT} · flow matching unit · predicted",
        f"{MLAT} · diffusion (VDM) · predicted",
        "Current literature: RLHF, DPO · predicted",
        "Current literature: reasoning models · predicted",
        "Current literature: MoE, Mamba · predicted",
        "AI for science literature; NeuralDEM · predicted",
    ],
    "s11_mlat": [
        f"{MLAT} (Brandstetter) · diffusion · exam July 2024, Q1",
        f"{MLAT} (Brandstetter) · hierarchical VAE · exam July 2024",
        f"{MLAT} (Brandstetter) · VAE · exam July 2024",
        f"{MLAT} (Brandstetter) · Neural ODEs · exam July 2024",
        f"{MLAT} (Brandstetter) · neural PDE surrogates · exam July 2024",
        f"{MLAT} (Brandstetter) · probabilistic PCA · exam July 2024",
        f"{MLAT} (Holzleitner) · estimators · exams 2024 and 2026",
        f"{MLAT} (Holzleitner) · Fisher information · exams 2024, 2026, retry",
        f"{MLAT} (Holzleitner) · statistical learning theory · exams 2024 and 2026",
        f"{MLAT} (Holzleitner) · VC dimension · exams 2024 and 2026",
        f"{MLAT} (Holzleitner) · kernels, RKHS · exam July 2026",
        f"{MLAT} (Holzleitner) · EM, maximum entropy · exam 2026, retry",
        f"{MLAT} (Holzleitner) · causality · exam July 2026",
    ],
}
beg = re.compile(r"\\begin\{qabox\}(?:\[[^\]]*\])?\{.*\}\n(\\from\{.*\}\n)?")
for f, items in FROM.items():
    p = os.path.join(HERE, f + ".tex")
    s = open(p, encoding="utf-8").read()
    n = len(beg.findall(s))
    assert n == len(items), (f, n, len(items))
    it = iter(items)
    s = beg.sub(lambda m: m.group(0).replace(m.group(1) or "", "") + "\\from{" + next(it) + "}\n", s)
    open(p, "w", encoding="utf-8").write(s)
    print(f, n)

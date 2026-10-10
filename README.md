# Defense Study Book

Study notes for the Master's examination in Artificial Intelligence:
Machine Learning & Perception, LSTM and sequence models, and recurrence CFD.

**Read online:** https://eigenzayn.github.io/defense-study-book/  
**Presentation (slides):** https://eigenzayn.github.io/defense-study-book/presentation/ (keys: arrows, P presenter, O overview, F fullscreen; PDF backup in `presentation/`)  
**Read the PDF:** [Defense_Study_Book.pdf](Defense_Study_Book.pdf)  
**Spoken answers (oral exam):** website https://eigenzayn.github.io/defense-study-book/oral_exam_v2/ (filter: asked before / predicted, search, practice mode) and PDF [oral_exam_v2/oral_exam_v2.pdf](oral_exam_v2/oral_exam_v2.pdf): thesis, Machine Learning & Perception and AI for Simulation (rCFD). Each answer has a core sentence, a short explanation, the numbers to know, a line-by-line derivation with the reason for each step, and a summary. Every question is labelled ASKED BEFORE (in the list of past defenses, with the examiner) or PREDICTED. Build: `cd oral_exam_v2 && python add_origins.py && pdflatex oral_exam_v2.tex` (twice) `&& python to_html.py`.

Each topic has four layers:

1. **2-minute summary**: the one idea, the one formula, the key words
2. **Picture it**: an everyday analogy to remember the idea
3. **Board drill**: the formula to write by hand three times
4. **Questions**: what to say, what to write, and the usual follow-up

Extra chapters: **conversation chains** (each answer ends with a hook to the next topic) and **hot topics and the Linz school** (xLSTM, Hopfield, SELU, RUDDER, NeuralDEM, reasoning LLMs, flow matching).

Sources are the JKU lecture scripts (Deep Learning and Neural Networks I/II, LSTM lecture)
and the Numerical Methods in Fluid Mechanics lecture.

Build: `cd book && pdflatex study_book.tex` (twice).

Every question carries a priority label: ASKED BEFORE (past defenses), COURSE EXAM, or PREDICTED, plus a "From:" line with course, chapter and origin.

Chapters also cover ML: Advanced Techniques (Brandstetter, Holzleitner) and the 2025 courses (Geometric DL, ML Unsupervised, DL Architectures).

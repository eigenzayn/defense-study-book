# Examiner questions: thesis part (model answers, max three sentences)

Answer first, then the reason, then stop. Numbers are from the thesis (claim_evidence_matrix.md).
"I do not know" is allowed: "I did not test that. What I can say is ..."

## Contribution and novelty
1. **What is new?** — The thesis tests rCFD on a scalar that drives its own flow, measures the trade-off of the standard mixing constant and its cause, and adds a bounded, conservative anti-diffusive correction to the replay. Earlier rCFD work carried passive scalars or weakly coupled heat. The limit of local corrections under a cooled lid is also new.
2. **rCFD has done heat transfer before (fluidised beds). Why is yours different?** — There the particle temperature hardly changes the gas flow. Here the temperature makes the flow, so the replay misses a feedback that is central, and I measured what that costs.

## Reference and fairness
3. **Why is the comparison fair?** — The reference and the recording are the same CFD run, so in the adiabatic case every difference is caused by the replay machinery. Both are read at the same instant, and end values use the same 20 s window.
4. **Why trust the reference?** — It is a laminar run at Re about 100 with the declared case settings; the comparison is replay against its own CFD, not against an experiment.

## Method
5. **What is in the database?** — Cell-to-cell maps for each of 600 frames, the recurrence matrix, topology data, and optional recorded fields: the recorded diffusivity and, added here, the recorded vertical heat flux.
6. **Why no recurrence jumps?** — Neither recording recurs: the recurrence prominence median is 0.028 and 0.027, below the 0.05–0.1 the method asks for. So the replay steps through the frames in order; it is still rCFD in the data-based sense.
7. **What does f_sd mean physically?** — It is the share of the temperature difference exchanged across each face per step; f_sd = 0.5 is equivalent to a diffusivity of 2.5e-7 m²/s on this mesh, ten times the molecular value.

## Numerical diffusion and the correction
8. **Where does the smearing come from?** — From the face exchange, not from the maps: with the maps alone the front stays 2.5 / 1.9 / 4.3 mm.
9. **Why not simply use negative diffusion?** — It is ill-posed: the shortest mode grows fastest; on the model front a 1 mK disturbance leaves the data range by more than 1 K after 21 steps.
10. **Is the correction conservative and bounded?** — Conservative by construction, every face moves energy from one cell to the other. Strictly bounded without the final clamp for s ≤ 1/6; the working range 0.4–0.5 relies on the clamp and the global conservation constraint.
11. **Why the vertical weight?** — Exchanges along the front amplify ripples; the squared-cosine weight is the face coefficient of a diffusion tensor along the front normal, so the correction acts only across the front.
12. **How sensitive is the result to s?** — Over s = 0.40–0.50 the end front is 5.3–4.5 mm and the trace error 0.70–0.64 K; small strengths (≤ 1/6) repair the trace but barely the front.

## Recorded fields
13. **Why does the recorded diffusivity not help?** — On this mesh and step every recorded value lies above the cap of the explicit exchange, so it acts as the constant 0.5; the outputs are bit-identical.
14. **Is the recorded flux cheating?** — It contains the reference's own temperature, so it is valid only for its case. I use it as a diagnostic: it proves that the remaining error is transport.

## Numerical error vs missing physics
15. **How do you separate them?** — In the adiabatic case the recording and the reference are the same flow, so all error is numerical. Under the cooled lid the boundary condition acts on a field the replay moves itself; what local, conservative fixes cannot remove is missing transport.

## Cost and transfer
16. **Does 260x include the recording?** — No. It is solver time against solver time; the recording costs one full run.
17. **Would it work for a turbulent or multiphase flow?** — Not shown. The front correction is local and should carry over, but the database must cover the regime, and that must be tested per case.
18. **What about the through-flow vessel (Q5)?** — The runs are in progress; I do not claim a result.

## Hardest follow-ups
19. **Your best number (+0.06 K) is one rung of a ladder you chose with the reference. Is this predictive?** — No, it is in-sample. The range s = 0.475–0.55 gives −0.04 to +0.06 K; a predictive choice of s is future work.
20. **What would you do differently?** — Record the flux without the reference temperature so it can transfer, and design the strength selection from the start.

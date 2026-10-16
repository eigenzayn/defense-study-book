# Thesis defense: English speaker notes

Generated from `defense/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Can a recorded flow carry a temperature that pushes back? (0:45, cumulative 0:45, 67 words)

**Cues:** record & replay · temperature drives the flow · where it breaks

Recurrence CFD records how a flow moves and replays that motion to carry a scalar, much faster than a new simulation. It was developed for scalars that do not act on the flow, like a dye. Temperature is different: warm water rises, so the temperature drives the flow that carries it. My thesis asks whether a replay can still carry such a temperature, and where it breaks.

**Key message:** The thesis tests a replay method on a scalar that drives its own flow.

**If you lose your place:** Replay works for dyes. Does it work for heat?

**Transition:** Let me show you the flow first.

## A warm jet builds a front only five millimetres thick (1:15, cumulative 2:00, 85 words)

**Cues:** jet for 315 s · 5 mm front · outlet under the front

Here is the test case. A warm jet enters a closed tank of cold liquid at mid height for 315 seconds. It rises, spreads under the lid, and builds a warm layer over the cold water. The front between the two layers is only about five millimetres thick. The flow is laminar, with a Reynolds number of about one hundred, so there is no turbulence model to argue about. Watch the outlet: it sits just below the front. That detail will matter in a minute.

**Key message:** A thin front forms, and the outlet sits just below it.

**If you lose your place:** Jet, thin front, outlet just below.

**Transition:** Simulating this costs hours. Here is the shortcut.

## rCFD records the motion once and replays it about 260 times cheaper (1:30, cumulative 3:30, 93 words)

**Cues:** maps, frame by frame · no pressure solve · 260x, recording excluded

Recurrence CFD works in two stages. The preparation runs the full simulation once and stores, frame by frame, where the fluid in each cell goes. The replay applies those stored maps to the temperature, adds a face exchange for mixing, an optional correction, and a conservation step. It never solves for velocity or pressure, so the feedback of temperature on the flow is cut. Solver time drops from 569 minutes to about two minutes. To be fair: the recording itself is one full run, and the ratio is solver time against solver time.

**Key message:** Record once, replay cheaply, but the feedback is cut.

**If you lose your place:** Maps, no pressure solve, 260 times.

**Transition:** The replay has one free knob, and that is my first question.

## One mixing knob cannot fix heat content and layer height at once (1:30, cumulative 5:00, 70 words)

**Cues:** f_sd is free · heat vs height · more mixing, more loss

The face exchange has a strength, f s d, that the user sets by hand. I swept seven values. With no added mixing, the mean temperature is best, about one kelvin of error. Near 0.5, the height of the warm layer is best. No single value gets both right. And more mixing makes the tank lose heat after the inflow: with the strongest mixing it ends five kelvin too cold.

**Key message:** No single f_sd is best; more mixing loses more heat.

**If you lose your place:** Heat versus height, no single best value.

**Transition:** Why does mixing lose heat? The answer sits at the outlet.

## The exchange smears the front, and the outlet below it drains the heat (1:30, cumulative 6:30, 86 words)

**Cues:** maps keep it thin · exchange smears · outlet drains

On the left is the reference, on the right the standard replay, from the same recorded motion. The replay's front is about four times thicker. If I switch the exchange off, the front stays thin, so the recorded maps are not the problem. The exchange is. And because the outlet sits just below the front, a thick front puts warm fluid at the outlet, and that heat leaves the tank. I recovered the outlet temperature from the energy balance and checked it against the stored fields.

**Key message:** The exchange, not the maps, smears the front; the outlet drains the heat.

**If you lose your place:** Maps fine, exchange smears, outlet drains.

**Transition:** If the exchange smears the front, can we undo it safely?

## A bounded anti-diffusion rebuilds the front without new extremes (1:45, cumulative 8:15, 99 words)

**Cues:** backward diffusion explodes · local bounds · vertical weight

The obvious repair is diffusion backwards. It steepens a front, but it also amplifies every small wiggle, as you can see on the left. So the correction is bounded. Each face may move heat up the gradient only as far as both cells stay inside the range of their neighbours. A local maximum cannot grow, a minimum cannot sink, and the energy moved out of one cell goes into the other. The idea follows flux-corrected transport. In the tank I weight the faces across the front, here the vertical ones, so that ripples along the front are not amplified.

**Key message:** Up-gradient, but bounded and conservative.

**If you lose your place:** Backward diffusion explodes; bounded version does not.

**Transition:** Does it work on the real tank?

## In the adiabatic tank the front returns to the width of the reference (1:30, cumulative 9:45, 70 words)

**Cues:** 15.7 to about 5 · error halves · s chosen against the reference

In the adiabatic tank the uncorrected front ends almost sixteen millimetres wide. Over the working range of the correction it ends between 5.3 and 4.5 millimetres, around the 5.0 of the reference. The error of the mean temperature falls from 1.5 to about 0.65 kelvin, so it halves. One honest point: I chose this strength range by comparing with the same reference. Choosing it without a reference is open work.

**Key message:** The front width returns; the strength was chosen against the reference.

**If you lose your place:** Sixteen to five millimetres, error halves.

**Transition:** That was an adiabatic tank. What happens when the lid loses heat?

## Under a cooled lid the heat is right, but the layers separate too slowly (1:45, cumulative 11:30, 95 words)

**Cues:** heat right · layers too slow · flux helps, overcools

Now the lid loses heat, so the temperature creates its own motion: cold plumes fall from the lid. With the declared wall coefficient, the standard replay ends 0.66 kelvin below the reference on almost ten kelvin of cooling. The correction brings the end to within 0.06 kelvin. But while the tank fills, the layers separate too slowly, and none of the local variants changed that. A vertical heat flux read from the recording removes most of this lag, from 2.25 to 0.45 kelvin. The price is that the tank then ends 0.86 kelvin too cold.

**Key message:** Heat right; the remaining error is missing transport.

**If you lose your place:** Heat right, layers too slow, flux helps but overcools.

**Transition:** Why can the recording not supply this by itself?

## A recording belongs to the flow regime it was made in (0:45, cumulative 12:15, 56 words)

**Cues:** own convection · ten times faster · one database per regime

The cooled lid drives its own convection. After the inflow, that flow changes about ten times faster than the adiabatic one at short time lags. A recording made without the cooling does not contain this motion, and no wall coefficient brings it back. So a database belongs to a flow regime, not to a single case.

**Key message:** One database per flow regime.

**If you lose your place:** Own convection, ten times faster.

**Transition:** So what does all this establish?

## What the evidence supports, and what it does not (1:15, cumulative 13:30, 71 words)

**Cues:** four supported · three open · vessel running

Let me separate what is shown from what is not. Shown: there is no single mixing strength, and the drain at the outlet is the reason. A conservative, bounded correction rebuilds the front. Under cooling, what remains is missing transport. And a database belongs to its regime. Not shown: a strength chosen without the reference, other meshes or turbulent flows, and the through-flow vessel, where the runs are still in progress.

**Key message:** Four results shown, the limits stated.

**If you lose your place:** Four shown, three open.

**Transition:** To close, the contribution in three lines.

## Contribution in three lines (0:45, cumulative 14:15, 45 words)

**Cues:** trade-off and cause · bounded correction · limit of local fixes

First, I measured the trade-off in the standard replay and found its cause. Second, I built a bounded, conservative correction that rebuilds the front. Third, I located the limit of local fixes: what remains is transport, and a recording belongs to its regime. Thank you.

**Key message:** Trade-off, correction, limit.

**If you lose your place:** Three lines, then thank you.



---
Planned speaking time: 14:15.
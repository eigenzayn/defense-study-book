# Thesis defense: English speaker notes

Generated from `defense/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Can a recorded flow carry a temperature that pushes back? (0:45, cumulative 0:45, 69 words)

**Cues:** record & replay · temperature drives the flow · where it breaks

Recurrence CFD records how a flow moves. Then it replays that motion to carry something, like a dye. This is much faster than a new simulation. But it was built for things that do not change the flow. Temperature is different. Warm water rises, so the temperature moves the flow. So my question is simple. Can a replay still carry a temperature like this? And where does it break?

**Key message:** I test a replay method on a temperature that moves its own flow.

**If you lose your place:** Replay works for a dye. Does it work for heat?

**Transition:** Let me show you the flow first.

## A warm jet builds a front only five millimetres thick (1:15, cumulative 2:00, 85 words)

**Cues:** jet for 315 s · 5 mm front · outlet under the front

Here is my test case. A warm jet comes into a closed tank of cold liquid. It comes in at mid height, for 315 seconds. The warm water rises and spreads under the lid. So we get a warm layer on top of cold water. Between them there is a front. It is only about five millimetres thick. The flow is laminar, so I need no turbulence model. Please look at the outlet. It sits just below the front. We will come back to that.

**Key message:** A thin front forms, and the outlet sits just below it.

**If you lose your place:** Jet, thin front, outlet just below.

**Transition:** This simulation is expensive. Here is the shortcut.

## rCFD records the motion once and replays it about 260 times cheaper (1:30, cumulative 3:30, 79 words)

**Cues:** maps, frame by frame · no pressure solve · 260x, recording excluded

The method has two steps. First, the full simulation runs once. While it runs, it stores where the fluid in each cell goes. Second, the replay uses these stored maps to move the temperature. It also mixes a little at every cell face, and it keeps the total heat right. It never solves for velocity or pressure. So it is much cheaper. 569 minutes become about two minutes. But to be fair, the recording itself costs one full run.

**Key message:** Record once, replay cheaply, but the feedback is cut.

**If you lose your place:** Store the maps, skip the pressure, 260 times faster.

**Transition:** The replay has one free setting. That is my first question.

## One mixing knob cannot fix heat content and layer height at once (1:30, cumulative 5:00, 71 words)

**Cues:** f_sd is free · heat vs height · more mixing, more loss

The mixing step has one strength. The user picks it by hand. I tried seven values. With no extra mixing, the heat content is best. With a strength near one half, the height of the warm layer is best. So no single value is good for both. And there is more. With more mixing, the tank loses heat after the inflow. With the strongest mixing, it ends five kelvin too cold.

**Key message:** No single mixing strength is best; more mixing loses more heat.

**If you lose your place:** Heat or height, not both.

**Transition:** Why does mixing lose heat? The answer is at the outlet.

## The exchange smears the front, and the outlet below it drains the heat (1:30, cumulative 6:30, 82 words)

**Cues:** maps keep it thin · exchange smears · outlet drains

On the left is the reference. On the right is the standard replay. Both use the same recorded motion. But the replay's front is about four times thicker. When I switch the mixing off, the front stays thin. So the stored maps are fine. The mixing step is the problem. Now remember the outlet. It sits just below the front. A thick front puts warm water at the outlet. And that heat leaves the tank. I checked this with the energy balance.

**Key message:** The mixing step, not the maps, smears the front, and the outlet drains the heat.

**If you lose your place:** Maps fine, mixing smears, outlet drains.

**Transition:** So can we undo the smearing safely?

## A bounded anti-diffusion rebuilds the front without new extremes (1:45, cumulative 8:15, 95 words)

**Cues:** backward diffusion explodes · local bounds · vertical weight

The obvious idea is to run diffusion backwards. That makes the front sharp again. But it also makes every small wiggle grow. You can see that on the left. So my correction has limits. Each face may move heat from cold to warm. But only so far that both cells stay inside the range of their neighbours. So no new hot spot and no new cold spot can appear. And the heat that leaves one cell goes into the other. In the tank, I only use the vertical faces. That stops ripples along the front.

**Key message:** Sharpen the front, but within limits and without losing heat.

**If you lose your place:** Backwards diffusion explodes; the limited version does not.

**Transition:** Does it work in the real tank?

## In the adiabatic tank the front returns to the width of the reference (1:30, cumulative 9:45, 61 words)

**Cues:** 15.7 to about 5 · error halves · s chosen against the reference

Without the correction, the front ends almost sixteen millimetres wide. With the correction, it ends between 5.3 and 4.5 millimetres. The reference has 5.0. So the width is back. The error of the mean temperature is about half as large. One honest point. I chose the strength by comparing with this same reference. Choosing it without the reference is still open.

**Key message:** The width comes back; the strength was chosen with the reference.

**If you lose your place:** Sixteen to five millimetres, error halves.

**Transition:** That tank had no heat loss. Now the lid gets cold.

## Under a cooled lid the heat is right, but the layers separate too slowly (1:45, cumulative 11:30, 96 words)

**Cues:** heat right · layers too slow · flux helps, overcools

Now the lid loses heat. Cold water sinks from the lid, so the temperature makes its own motion. With the declared wall setting, the standard replay ends 0.66 kelvin too cold. That is on almost ten kelvin of cooling. With the correction, it ends within 0.06 kelvin. So the heat is right. But while the tank fills, the layers separate too slowly. No local fix changed that. Then I read a heat flux from the recording. It removes most of the delay, from 2.25 to 0.45 kelvin. But the tank then ends 0.86 kelvin too cold.

**Key message:** The heat is right; what is missing is transport.

**If you lose your place:** Heat right, layers too slow, flux helps but overcools.

**Transition:** Why can the recording not do this by itself?

## A recording belongs to the flow regime it was made in (0:45, cumulative 12:15, 37 words)

**Cues:** own convection · ten times faster · one database per regime

The cold lid creates its own movement. After the inflow, this flow changes about ten times faster. A recording without the cold lid does not contain this movement. So a recording belongs to one type of flow.

**Key message:** One recording per type of flow.

**If you lose your place:** Own movement, ten times faster.

**Transition:** So what does all this show?

## What the evidence supports, and what it does not (1:15, cumulative 13:30, 71 words)

**Cues:** four supported · three open · vessel running

Let me be clear about what I showed. One: no single mixing strength works, and the outlet explains why. Two: a limited correction rebuilds the front. Three: with a cold lid, what remains is missing transport. Four: a recording belongs to its type of flow. And what I did not show. A strength chosen without the reference. Other meshes or turbulent flows. And the through-flow vessel. Those runs are still going.

**Key message:** Four results shown, the limits stated.

**If you lose your place:** Four shown, three open.

**Transition:** To close, my contribution in three lines.

## Contribution in three lines (0:45, cumulative 14:15, 45 words)

**Cues:** trade-off and cause · bounded correction · limit of local fixes

First, I measured the problem of the standard replay and found its cause. Second, I built a limited correction that rebuilds the front. Third, I found where local fixes stop. What remains is transport, and a recording belongs to its type of flow. Thank you.

**Key message:** Problem and cause, correction, limit.

**If you lose your place:** Three lines, then thank you.



---
Planned speaking time: 14:15.
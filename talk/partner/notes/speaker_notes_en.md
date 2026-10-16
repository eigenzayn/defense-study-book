# Industrial partner talk: English speaker notes

Generated from `partner/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Thermal processes are fast in flow and slow in temperature (0:45, cumulative 0:45, 39 words)

**Cues:** two time scales · CFD pays for both · my starting point

In many thermal processes the flow reaches its pattern within seconds, but the temperature it carries keeps changing for minutes or hours. Simulation has to resolve the fast part the whole time. That mismatch is where my research starts.

**Key message:** Two time scales; we pay for the fast one.

**If you lose your place:** Flow fast, temperature slow.

**Transition:** Here is what that costs.

## Simulating hours of a process is the expensive part (1:15, cumulative 2:00, 83 words)

**Cues:** 569 minutes · pressure solve dominates · temperature is cheap

In my test case, about ten minutes of flow cost about nine and a half hours of solver time. Most of that goes into velocity and pressure, which the solver couples again in every step, even after the flow has settled. The temperature itself is cheap. So the question I asked was simple: can we keep the temperature physics and stop paying for the flow every time? The answer depends on whether the temperature changes the flow, and that is what I tested.

**Key message:** The cost is the flow, not the temperature.

**If you lose your place:** 569 minutes, mostly pressure.

**Transition:** There is a method that does exactly this.

## Record the flow once, replay it for the temperature (1:30, cumulative 3:30, 67 words)

**Cues:** maps · 260x after one recording · feedback cut

Recurrence CFD records, once, how the fluid moves from cell to cell. After that, the replay only applies these stored maps to the temperature, with a mixing step and a conservation step. It is about 260 times cheaper in solver time, after one full recording run. The catch is that the replay cannot let the temperature change the flow, because the flow is fixed in the recording.

**Key message:** Record once, replay cheaply, feedback cut.

**If you lose your place:** Maps, 260 times, the catch.

**Transition:** So I built a case where the temperature does push back.

## A small tank where the temperature pushes back (1:30, cumulative 5:00, 69 words)

**Cues:** same flow · thick front · that is the defect

This is that case. A warm jet fills a closed tank and builds a warm layer over cold water. On the left is the full simulation, on the right the replay with standard settings, from the same recorded flow. The front between the layers is about five millimetres in the reference, and about four times thicker in the replay. That thick front is the defect I had to explain.

**Key message:** Same flow, thick front.

**If you lose your place:** Same flow, four times thicker front.

**Transition:** How did I find out why?

## How I found the error: from the tank budget down to one face (1:45, cumulative 6:45, 74 words)

**Cues:** follow the heat · outlet under the front · the mixing step

I did not tune my way out of it. I followed the heat. First the tank budget: no mixing strength gets both the heat content and the layer height right. Then the outlet, which I reconstructed from the energy balance: a smeared front puts warm fluid at the outlet height, and that heat leaves the tank. Finally one face between two cells: the recorded maps keep the front thin, the mixing step smears it.

**Key message:** Budget, outlet, face.

**If you lose your place:** Follow the heat to one face.

**Transition:** Once the cause is local, the fix can be local too.

## A correction that respects physics (1:30, cumulative 8:15, 74 words)

**Cues:** up-gradient, bounded · conserves energy · honest about tuning

The fix moves heat back up the gradient, but each face only as far as both cells stay inside the range of their neighbours. So it conserves energy and cannot invent a new hot or cold spot. The front returns from almost sixteen millimetres to about five, close to the reference. I want to be clear: I chose its strength by comparing with the reference. Choosing it without one is the next research step.

**Key message:** Bounded and conservative; honest about tuning.

**If you lose your place:** Sixteen to five millimetres, within bounds.

**Transition:** Then I made the problem harder.

## Knowing the limit is part of the result (1:30, cumulative 9:45, 81 words)

**Cues:** heat right · transport missing · one regime per database

With a cooled lid, the temperature creates its own motion. The correction gets the heat content right, within 0.06 kelvin. But while the tank fills, the layers separate too slowly, and no local fix changes that. Reading a heat flux from the recording removes most of the lag, but the tank then ends too cold. So what remains is missing transport, and a recording only serves the regime it was made in. For me that is a result, not a failure.

**Key message:** Heat right, transport missing.

**If you lose your place:** Heat right, transport missing.

**Transition:** This is where I see room for scientific machine learning.

## Where scientific machine learning could fit (1:45, cumulative 11:30, 73 words)

**Cues:** learn the closure · regime-aware · physics as tests

Three directions follow from what I measured, and none of them is tested yet. First, learn the mixing term from data instead of setting it by hand. Second, choose or blend recordings according to the state of the flow, because one recording serves one regime. Third, use conservation, boundedness and the energy budget as acceptance tests for any fast model. The reference flow also looks low-dimensional: two modes hold most of its variance.

**Key message:** Each direction comes from a measured weakness.

**If you lose your place:** Learn, regime-aware, physics tests.

**Transition:** Before any of this touches a process, it must pass some tests.

## What must be validated before an industrial use (1:45, cumulative 13:15, 64 words)

**Cues:** physics gap · regime coverage · measured validation

My tank is laminar and single-phase. An industrial reactor is neither. So before anything like this is used on a process, it must be shown on that process's own physics: reference data per regime and its cost, recordings that cover the relevant motions, conservation, the error on the quantity that matters, and comparison with measurements. A lab-rig study of this kind is running now.

**Key message:** Validate on the process's own physics.

**If you lose your place:** Physics gap, coverage, measurements.

**Transition:** Let me close with how I work.

## How I work, and the next question (1:00, cumulative 14:15, 51 words)

**Cues:** follow the budget · fix within bounds · state the limit

That is how I work. I follow the energy budget until the error has a location. I fix it within physical bounds. And I say where the method stops, with numbers. The next question I would like to answer is whether the replay can choose its own correction strength. Thank you.

**Key message:** Budget, bounds, limits.

**If you lose your place:** Three habits, one question.



---
Planned speaking time: 14:15.
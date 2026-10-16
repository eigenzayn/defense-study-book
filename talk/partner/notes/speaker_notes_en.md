# Industrial partner talk: English speaker notes

Generated from `partner/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Thermal processes are fast in flow and slow in temperature (0:45, cumulative 0:45, 35 words)

**Cues:** two time scales · CFD pays for both · my starting point

In many processes, the flow finds its pattern in seconds. But the temperature keeps changing for minutes or hours. Simulation has to follow the fast part all the time. That is where my research starts.

**Key message:** Two time scales; we pay for the fast one.

**If you lose your place:** Flow fast, temperature slow.

**Transition:** Here is what that costs.

## Simulating hours of a process is the expensive part (1:15, cumulative 2:00, 75 words)

**Cues:** 569 minutes · pressure solve dominates · temperature is cheap

In my test case, ten minutes of flow took about nine and a half hours to simulate. Most of that time goes into velocity and pressure. The solver repeats this in every step, even when the flow has settled. The temperature itself is cheap. So my question was simple. Can we keep the temperature physics, and stop paying for the flow every time? The answer depends on one thing. Does the temperature change the flow?

**Key message:** The cost is the flow, not the temperature.

**If you lose your place:** 569 minutes, mostly pressure.

**Transition:** There is a method that does exactly this.

## Record the flow once, replay it for the temperature (1:30, cumulative 3:30, 66 words)

**Cues:** maps · 260x after one recording · feedback cut

The method records the flow once. It stores how the fluid moves from cell to cell. After that, the replay only moves the temperature with these stored maps. It is about 260 times cheaper. But you need one full simulation first, to record the maps. And there is a catch. The replay cannot let the temperature change the flow. The flow is fixed in the recording.

**Key message:** Record once, replay cheaply, feedback cut.

**If you lose your place:** Maps, 260 times, the catch.

**Transition:** So I built a case where the temperature does change the flow.

## A small tank where the temperature pushes back (1:30, cumulative 5:00, 67 words)

**Cues:** same flow · thick front · that is the defect

This is that case. A warm jet fills a closed tank. It builds a warm layer on top of cold water. On the left is the full simulation. On the right is the replay with standard settings. Same recorded flow. In the reference, the front is about five millimetres thick. In the replay, it is about four times thicker. That is the problem I had to explain.

**Key message:** Same flow, thick front.

**If you lose your place:** Same flow, front four times thicker.

**Transition:** How did I find the cause?

## How I found the error: from the tank budget down to one face (1:45, cumulative 6:45, 74 words)

**Cues:** follow the heat · outlet under the front · the mixing step

I did not just tune numbers until it looked right. I followed the heat. First, the whole tank. No mixing setting gets both the heat and the layer height right. Then the outlet. I calculated its temperature from the energy balance. A thick front puts warm water at the outlet. So heat leaves the tank. Finally, one face between two cells. The stored maps keep the front thin. The mixing step makes it thick.

**Key message:** Tank, outlet, one face.

**If you lose your place:** Follow the heat to one face.

**Transition:** Once the cause is local, the fix can be local too.

## A correction that respects physics (1:30, cumulative 8:15, 77 words)

**Cues:** up-gradient, bounded · conserves energy · honest about tuning

The fix moves heat back, from cold to warm. But each face only moves so much that both cells stay within their neighbours' range. So it keeps the total heat. And it cannot create a new hot or cold spot. The front goes back from almost sixteen to about five millimetres. That is close to the reference. To be honest, I chose the strength by comparing with the reference. Choosing it without one is the next step.

**Key message:** Limited and heat-conserving; honest about tuning.

**If you lose your place:** Sixteen to five millimetres, within limits.

**Transition:** Then I made the problem harder.

## Knowing the limit is part of the result (1:30, cumulative 9:45, 83 words)

**Cues:** heat right · transport missing · one regime per database

Now the lid gets cold. The temperature creates its own movement. The correction gets the heat right, within 0.06 kelvin. But while the tank fills, the layers separate too slowly. No local fix changes that. A heat flux read from the recording removes most of the delay. But then the tank ends too cold. So the missing piece is transport. And a recording only works for the type of flow it was made in. For me, that is a result, not a failure.

**Key message:** Heat right, transport missing.

**If you lose your place:** Heat right, transport missing.

**Transition:** This is where I see room for machine learning.

## Where scientific machine learning could fit (1:45, cumulative 11:30, 82 words)

**Cues:** learn the closure · regime-aware · physics as tests

Three ideas follow from what I measured. None of them is tested yet. First, learn the mixing strength from data, instead of setting it by hand. Second, choose the recording based on the state of the flow. One recording only covers one type of flow. Third, use simple physics checks as tests for any fast model. Does it keep the heat? Does it stay within limits? Also, the reference flow looks simple in one way. Two patterns hold most of its variation.

**Key message:** Each idea comes from a measured weakness.

**If you lose your place:** Learn, choose by state, physics tests.

**Transition:** Before any of this is used on a real process, it must pass some tests.

## What must be validated before an industrial use (1:45, cumulative 13:15, 85 words)

**Cues:** physics gap · regime coverage · measured validation

My tank is simple. The flow is laminar, and there is only one fluid. A real reactor is not like that. So first we would need to show a few things on the real process. We need reference data for each operating state, and we need to know what it costs. The recordings must cover the right movements. The method must keep the heat and stay within limits. And in the end, it must match real measurements. A lab study like this is running now.

**Key message:** Test on the process's own physics.

**If you lose your place:** Physics gap, coverage, measurements.

**Transition:** Let me close with how I work.

## How I work, and the next question (1:00, cumulative 14:15, 47 words)

**Cues:** follow the budget · fix within bounds · state the limit

So this is how I work. I follow the energy until I know where the error comes from. I fix it within physical limits. And I say clearly where the method stops. My next question is this. Can the replay choose its own correction strength? Thank you.

**Key message:** Follow the energy, fix within limits, state the limit.

**If you lose your place:** Three habits, one question.



---
Planned speaking time: 14:15.
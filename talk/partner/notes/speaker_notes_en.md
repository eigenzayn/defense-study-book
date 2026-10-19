# Industrial partner talk: English speaker notes

Generated from `partner/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Thermal processes are fast in flow and slow in temperature (0:45, cumulative 0:45, 77 words)

**Cues:** two clocks · we pay for the fast one · my starting point

Thank you for having me. Many thermal processes share one feature. There are two clocks running at the same time. The flow is the fast clock. It finds its pattern in seconds. The temperature is the slow clock. It keeps changing for minutes, sometimes for hours. But a normal simulation has to follow the fast clock all the time, even when nothing new happens in the flow. That is expensive. And that is where my research starts.

**Key message:** Two time scales; we pay for the fast one.

**If you lose your place:** Flow fast, temperature slow.

**Transition:** Here is what that costs.

## Simulating hours of a process is the expensive part (1:15, cumulative 2:00, 101 words)

**Cues:** 569 minutes · pressure every step · the question

Let me put a number on it. In my test case, about ten minutes of flow, in a tank of seventy-five millimetres, took 569 minutes of solver time. That is more than nine hours. Where does that time go? Mostly into velocity and pressure. In every time step, the solver couples them again, even after the flow has settled into its pattern. The temperature itself is cheap to carry. So the engineering question is simple. Can we keep the temperature physics, and stop paying for the flow every time? The answer depends on one thing. Does the temperature change the flow?

**Key message:** The cost is the flow, not the temperature.

**If you lose your place:** 569 minutes, mostly pressure.

**Transition:** There is a method that does exactly this.

## Record the flow once, replay it for the temperature (1:30, cumulative 3:30, 159 words)

**Cues:** simulate once · record the motion · replay, 260x

There is a method that does exactly this. It is called recurrence CFD, and it works in three steps. Step one: simulate once. One full simulation, with velocity, pressure and temperature. Step two: record the motion. For every second, we store where the fluid in each cell goes. Six hundred frames. Think of a traffic camera that records the route of every car in a city. Step three: replay. We use those stored routes to move the temperature, and we never solve for velocity or pressure again. In my case, one replay takes about two minutes. That is roughly 260 times cheaper. To be fair, you need the full simulation first, so the saving starts with the second replay. But there is a catch. What if the parcels you move are so heavy that they change the traffic? That is temperature. Warm water rises. In the replay, the flow is fixed, so the temperature can no longer change it.

**Key message:** Record once, replay cheaply, feedback cut.

**If you lose your place:** Simulate, record, replay. 260 times. The catch.

**Transition:** So I built a case where the temperature does change the flow.

## A small tank where the temperature pushes back (1:30, cumulative 5:00, 113 words)

**Cues:** warm jet, thin front · same recorded flow · four times thicker

So I built a case where the temperature does change the flow. A warm jet enters a closed tank, for 315 seconds. It builds a warm layer on top of cold water, with a thin front in between. On the left, the full simulation. On the right, the replay with its standard settings. Same recorded flow. Now look at the front. In the full simulation, it is about five millimetres thick. In the replay, it is about four times thicker. The tank is laminar and closed, so every joule in and out can be accounted for. That makes it a clean place to ask the real question. Where does this error come from?

**Key message:** Same flow, thick front.

**If you lose your place:** Five millimetres, four times thicker.

**Transition:** How did I find the cause?

## The outlet below the front turns a smeared front into a heat leak (1:45, cumulative 6:45, 129 words)

**Cues:** followed the heat · outlet below the front · mixing, not recording

I did not tune numbers until the picture looked right. I followed the heat. First, the whole tank: no setting of the mixing knob gets both the heat and the layer height right. Then the outlet. I recovered its temperature from the energy balance of the tank. And here is the key. The outlet sits just below the front. So a thick front puts warm water at the outlet, and after the inflow, 4.6 kelvin of mean temperature drains away. Finally, one face between two cells. With the recorded motion alone, the front stays thin. With the mixing step, it gets thick. So the recording is fine. The mixing step is the problem. That is how I like to work. Follow the energy, until the error has an address.

**Key message:** Outlet below the front: a smeared front leaks heat.

**If you lose your place:** Follow the heat to the outlet.

**Transition:** Once the cause is local, the fix can be local too.

## A correction that respects physics (1:30, cumulative 8:15, 136 words)

**Cues:** uphill, within bounds · keeps the energy · honest about tuning

Once the cause is local, the fix can be local too. So I built a correction that respects physics. It moves heat back, from the colder cell to the warmer one, to sharpen the front. But each face only moves as much as both cells can take, while they stay within the range of their neighbours. So the total heat stays exactly the same, and no new hot spot or cold spot can appear. For an industrial model, I think this matters. A correction that you cannot trust to keep the energy is not a correction. The result? The front goes back from almost sixteen millimetres to about five. The full simulation has five. One honest note. I chose the strength by comparing with the full simulation. Choosing it without one is the next research step.

**Key message:** Limited and energy-conserving; honest about tuning.

**If you lose your place:** Sixteen to five millimetres, within limits.

**Transition:** Then I made the problem harder.

## Knowing the limit is part of the result (1:45, cumulative 10:00, 138 words)

**Cues:** cold lid, own motion · heat right, transport missing · one regime per recording

Then I made the problem harder. I made the lid cold. Look at the plumes. Cold water falls from the lid, so now the temperature creates its own motion. The correction still gets the heat content right. It ends within 0.06 kelvin, on almost ten kelvin of cooling. But while the tank fills, the layers separate too slowly, and no local fix changes that. The missing piece is transport. And there is a bigger lesson. These plumes are a motion that the insulated recording never saw. A recording only covers the kind of flow it was made in. Think of the traffic camera again. A recording of a quiet Sunday will not tell you how the city moves in a snowstorm. For me, knowing where a method stops is part of the result. It is not a failure.

**Key message:** Heat right, transport missing, one regime per recording.

**If you lose your place:** Sunday is not a snowstorm.

**Transition:** This is where I see room for machine learning.

## Where scientific machine learning could fit (2:00, cumulative 12:00, 143 words)

**Cues:** learn the mixing · switch by regime · physics as tests

This is where I see room for machine learning. Three directions, and each one comes from a weakness that I measured. I want to be clear: none of them is tested yet. First, learn the mixing. Today, a person sets the knob by hand. A model could learn it from recorded data, and we would check it against the full simulation. Second, switch by regime. One recording covers one kind of flow, so a replay could watch its own state and pick the right recording. Third, physics as tests. Any fast model, learned or not, should pass simple checks. Does it keep the energy? Does it stay within physical limits? And before anyone uses this on a real process, three things must be shown: reference data for each operating state, recordings that cover what the process will see, and checks against real measurements.

**Key message:** Each idea comes from a measured weakness; validation first.

**If you lose your place:** Learn, switch, test. Then validate.

**Transition:** Let me close with how I work.

## How I work, and the next question (1:00, cumulative 13:00, 64 words)

**Cues:** follow the energy · fix within bounds · state the limit

Let me close with how I work. One. I follow the energy until the error has a location. Two. I fix it within physical bounds. Three. I state clearly where the method stops, with numbers. And my next question is this. Can the replay choose its own correction strength, without a full simulation to compare with? Thank you. I look forward to your questions.

**Key message:** Follow the energy, fix within limits, state the limit.

**If you lose your place:** Three habits, one question.



---
Planned speaking time: 13:00.
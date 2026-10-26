# Thesis defense: English speaker notes

Generated from `defense/index.html` (the presenter window shows the same text). Speak, do not read:
the cues are enough once the story is clear. Planning rate about 120 words per minute.

## Can a recorded flow carry a temperature that pushes back? (0:45, cumulative 0:45, 113 words)

**Cues:** film the flow once · temperature pushes back · where does it break?

Thank you for coming. Imagine you could film how water moves through a tank, just once. And then, every time you need an answer, you simply replay that film, instead of solving the physics again. That is the idea behind recurrence CFD, and it is fast. Really fast. But there is a catch. The method was built for things that just ride along with the flow, like a drop of dye. Temperature is different. Warm water rises. So temperature pushes back on the very flow that carries it. And that is my question today. Can a recorded flow carry a temperature that pushes back? And if it cannot, where exactly does it break?

**Key message:** I test a replay method on a temperature that moves its own flow.

**If you lose your place:** Replay works for dye. Does it work for heat?

**Transition:** Let me show you the flow first.

## A warm jet builds a front only five millimetres thick (1:15, cumulative 2:00, 145 words)

**Cues:** jet for 315 s · 5 mm front · outlet under the front

Let me show you the flow first. This is my test case. A small, closed tank, seventy-five millimetres wide, full of cold liquid. At mid-height, a warm jet comes in, for 315 seconds. Now watch what happens. The warm water rises, spreads out under the lid, and slowly fills the tank from the top down. Between the warm layer and the cold water below, a front forms. And look how thin it is. Only about five millimetres. The flow is slow and smooth, with a Reynolds number of about one hundred. So it is laminar, and I need no turbulence model. And because the tank is closed, I can account for every joule that goes in and every joule that comes out. One more detail, and please keep it in mind: the outlet. It sits just below the front. We will come back to it.

**Key message:** A thin front forms, and the outlet sits just below it.

**If you lose your place:** Jet, thin front, outlet just below.

**Transition:** This simulation is expensive. Here is the shortcut.

## rCFD records the motion once and replays it about 260 times cheaper (1:30, cumulative 3:30, 183 words)

**Cues:** record the routes · replay moves heat · 260x, feedback cut

So how does the shortcut work? It has two steps. First, we run the full simulation once. And while it runs, we record, for every time step, where the fluid in each cell goes. Think of a traffic camera that records the route of every car in a city. Second, the replay. It takes those stored routes and uses them to move the temperature. It also mixes a little heat between neighbouring cells, and it keeps the total heat right. But it never solves for velocity or pressure again. That is why it is so cheap. In my case, the full simulation needed 569 minutes of solver time. One replay needs about two minutes. That is roughly 260 times faster. To be fair, the recording itself costs one full run, so the saving starts with the second replay. Now, here is the problem. Back to the traffic camera. What if the parcels you move are so heavy that they change the traffic? That is temperature. In the replay, the motion is fixed. The temperature can no longer change it. That feedback is cut.

**Key message:** Record once, replay cheaply, but the feedback is cut.

**If you lose your place:** Store the routes, skip the pressure, 260 times faster, feedback cut.

**Transition:** The replay has one free setting. That is my first question.

## One mixing knob cannot fix heat content and layer height at once (1:30, cumulative 5:00, 175 words)

**Cues:** one knob, seven values · heat or height · more mixing, more loss

The replay has one free setting. After each move, it mixes a bit of heat across every face between two cells. How much? That is a knob, and the user sets it by hand. So my first question was simple. What is the right setting? I tried seven values, from no extra mixing at all, up to strong mixing. On the left, you see the mean temperature of the tank. On the right, how high the heat sits. And here is the trouble. The heat content is best with no extra mixing. The error is 1.07 kelvin. But the height of the warm layer is best with a medium setting, around one half. There, the error is only 0.068 millimetres. So no single value gets both right. And it gets worse. The more you mix, the more heat the tank loses after the inflow stops. With the strongest mixing, the tank ends 5.08 kelvin too cold. So mixing does not just blur the picture. It changes the energy in the tank. The question is: why?

**Key message:** No single mixing strength is best; more mixing loses more heat.

**If you lose your place:** Heat or height, not both. Strong mixing ends 5 K too cold.

**Transition:** Why does mixing lose heat? The answer is at the outlet.

## The exchange smears the front, and the outlet below it drains the heat (1:30, cumulative 6:30, 164 words)

**Cues:** same motion, thick front · maps fine, mixing guilty · outlet drains heat

Here is the answer. On the left, the reference simulation. On the right, the standard replay. Both use exactly the same recorded motion. But look at the front. In the reference, at 240 seconds, it is 4.5 millimetres thick. In the replay, it is 19.3. More than four times thicker. So who is guilty? The recording, or the mixing? I tested that. When I switch the mixing off and keep only the recorded maps, the front stays thin: 2.5 millimetres. So the recording is fine. It is the mixing step that smears the front. Now, remember the outlet, just below the front. A thick front reaches down to the outlet. So warm water leaves the tank, and the heat leaves with it. I checked this with the energy balance of the whole tank. After the inflow, the smeared replay drains 4.6 kelvin of mean temperature through the outlet. So a small numerical error at the front becomes a real error in the energy budget.

**Key message:** The mixing step, not the maps, smears the front, and the outlet drains the heat.

**If you lose your place:** Maps fine, mixing smears, outlet drains.

**Transition:** So can we undo the smearing, safely?

## A bounded anti-diffusion rebuilds the front without new extremes (1:45, cumulative 8:15, 224 words)

**Cues:** backwards diffusion explodes · stay inside the neighbours · vertical, across the front

So, can we undo the smearing? The obvious idea is to run diffusion backwards. Diffusion makes things smooth, so negative diffusion should make them sharp again. And it does, for a moment. But it also makes every tiny wiggle grow, and the smallest wiggles grow the fastest. You can see it on the left. In this one-dimensional test, after just 21 steps, the field leaves the range of the data. That is useless. So I kept the useful part, and I stopped the dangerous part with a limit. My rule is this. Across each face, heat may move uphill, from the colder cell to the warmer one. That sharpens the front. But only so far that both cells stay inside the range of their neighbours. No cell may get hotter than its hottest neighbour, or colder than its coldest one. So no new hot spot and no new cold spot can appear. And whatever heat leaves one cell enters the other, so energy is conserved, face by face. This idea comes from flux-corrected transport, by Boris and Book, and by Zalesak. One last detail. The front is horizontal, so I let the correction act across the front, in the vertical direction, and not along it. On the right, the limited version simply sharpens the front, from 8.8 cells to 0.9, and then it stops.

**Key message:** Sharpen the front, but within limits and without losing heat.

**If you lose your place:** Backwards diffusion explodes; the limited version does not.

**Transition:** Does it work in the real tank?

## In the adiabatic tank the front returns to the width of the reference (1:30, cumulative 9:45, 133 words)

**Cues:** 15.7 to about 5 · error halves · chosen with the reference

Does it work in the real tank? Here is the end of the run. Without the correction, the front ends 15.7 millimetres wide. With the correction, in its working range, it ends between 5.3 and 4.5 millimetres. The reference has 5.0. So the width is back. You can see it in the pictures. The row below shows the departure from the reference. It shrinks as the strength grows, and it turns again when the correction gets too strong. And the error of the mean temperature over the whole run drops from 1.46 kelvin to about 0.7. I want to be honest about one point. I chose the strength by comparing with this same reference. So this shows what the correction can do. Choosing the strength without a reference is still an open question.

**Key message:** The width comes back; the strength was chosen with the reference.

**If you lose your place:** Sixteen to five millimetres, error halves, honest about s.

**Transition:** That tank had no heat loss. Now the lid gets cold.

## Under a cooled lid the heat is right, but the layers separate too slowly (1:45, cumulative 11:30, 189 words)

**Cues:** heat right · layers too slow · flux helps, overcools

So far, the lid was insulated. Now I make it cold, and this changes the story. Cold water sinks from the lid in plumes. So now the temperature creates its own motion. This is exactly the feedback that the replay cannot reproduce. Let's see what happens. Over the run, the tank cools by 9.62 kelvin. The standard replay ends 0.66 kelvin too cold. With the correction, it ends within 0.06 kelvin, again with a strength chosen against the reference. So the heat content is right. But look at the shaded band during the warm inflow. While the tank fills, the layers separate too slowly. I tried six different local corrections, and none of them moved this lag. Why not? Because a local rule only moves heat between neighbours. It can sharpen a front, but it cannot carry heat from one layer to another. That needs transport. So I read a vertical heat flux from the recording itself, and I added it to the replay. It removes most of the lag, from 2.25 to 0.45 kelvin. But it comes with a price. The tank then ends 0.86 kelvin too cold.

**Key message:** The heat is right; what is missing is transport.

**If you lose your place:** Heat right, layers too slow, flux helps but overcools.

**Transition:** Why can the recording not do this by itself?

## A recording belongs to the flow regime it was made in (0:45, cumulative 12:15, 96 words)

**Cues:** cold lid, own motion · ten times faster · one recording per regime

Why can the recording not do this by itself? Because the cold lid makes a different kind of flow. These maps compare every moment of a recording with every other moment. After the inflow, the cooled flow keeps renewing itself, about ten times faster than the insulated one. A recording made without the cold lid simply does not contain that motion. Think of the traffic camera again. A recording of a quiet Sunday will not tell you how the city moves in a snowstorm. So a recording belongs to the flow regime it was made in.

**Key message:** One recording per type of flow.

**If you lose your place:** Own motion, ten times faster, Sunday is not a snowstorm.

**Transition:** So what does all this show?

## What the evidence supports, and what it does not (1:15, cumulative 13:30, 112 words)

**Cues:** four shown · four open · vessel running

Let me be clear about what the evidence supports. One. There is no single best mixing setting, and the outlet below the front explains why. Two. A conservative, bounded correction rebuilds the front, without creating new extremes. Three. Under a cold lid, what remains is missing transport, not missing sharpness. And four. A recording belongs to its flow regime. Now, what I have not shown. I have not chosen the strength without the reference. I have not tested other meshes, turbulent flows, or several phases. The through-flow vessel study is still running, so I claim no result from it. And I have not shown that a recorded flux transfers to other cases.

**Key message:** Four results shown, the limits stated.

**If you lose your place:** Four shown, four open.

**Transition:** To close, three things to take home.

## Contribution in three lines (0:45, cumulative 14:15, 82 words)

**Cues:** trade-off and cause · bounded correction · limit of local fixes

So, three things to take home. One. I measured the trade-off of the standard replay, and I found its cause: a smeared front that drains heat through the outlet. Two. I built a correction that sharpens the front within physical bounds, without creating new extremes. Three. I found where local fixes stop. What remains is transport, and a recording belongs to its regime. A fast simulation is only useful when we know its error. That is what this thesis measures. Thank you.

**Key message:** Problem and cause, correction, limit.

**If you lose your place:** Three lines, then thank you.



---
Planned speaking time: 14:15.
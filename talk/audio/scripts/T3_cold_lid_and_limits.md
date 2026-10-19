# T3 · The cold lid, the limits, and how I know I am right

In this episode we go to the harder half of the thesis: the cooled lid. Then we practise the questions every committee asks at the end. How do you know your results are correct? What would you do differently? And which papers shaped your work?

## When the lid gets cold

Up to now, the lid was insulated. Heat came in with the jet and left through the outlet, and that was it. Now the lid loses heat to the outside. And this changes the physics. Cold water forms under the lid, it is heavier, so it sinks in plumes. The layer above the front starts to overturn. So now the temperature creates its own motion. That is exactly the feedback that a replay cannot reproduce, because the motion is fixed in the recording.

Every replay in this chapter uses the same fluid properties as the reference. Keep that sentence ready, because it rules out a whole family of questions.

## What the replay gets right

Over the run, the tank cools by 9.62 kelvin. The standard replay ends 0.66 kelvin too cold. That sounds small, and it is, for the heat content. But look at where the heat is. The end profile of the standard replay departs by 2.79 kelvin: the bulk is too warm, and the top layer is too cold. Same heat, wrong place.

With the correction, at strengths between 0.475 and 0.55, the end error of the heat content is between minus 0.04 and plus 0.06 kelvin, and the end profile improves to between 0.59 and 0.41 kelvin. So the correction puts the heat back in the right layer. And again, say it honestly: these strengths were chosen with the reference.

This is why I always report two kinds of measure. The mean temperature says how much heat there is. The profile and the front width say where it is. A replay can be right on one and wrong on the other.

## What cannot be repaired

Now the defect that survives. While the tank fills, the layers separate too slowly. I tried six local variants, and none of them moved this lag. Why?

Here is the cleanest way to say it. A local correction only moves heat between neighbours. It can change the shape of a front, but it cannot carry heat from one layer to another layer far away. That is transport. So the lag is missing transport, not missing sharpness.

Then I tried to supply that transport. During the recording, I stored a vertical heat flux: the part of the heat carried by the vertical velocity, relative to the mean of a horizontal band. In the replay, I applied it. And it works: the layering lag drops from 2.25 to 0.45 kelvin. But it has a price. The tank then ends 0.86 kelvin too cold.

## Why the recording cannot do it alone

The final piece of the story is the flow regime. Compare how fast each recording changes over short time lags. After the inflow, the cooled flow keeps renewing itself, about ten times faster than the insulated one. So a recording made without the cold lid simply does not contain the motion of the cooled case. A database belongs to a flow regime, not to a case. In machine learning language: a new regime is out of distribution.

## How do you know your results are correct?

This came up in earlier defenses. Give three short points.

First, every replay is deterministic. A rerun gives the same trace, bit for bit. So any difference between two runs comes from the one setting I changed.

Second, I compare replay and reference at the same instants, and over the same end window, from 580 to 599 seconds, on both sides.

Third, I close the energy budget of each case, term by term. If the heat does not add up, I know before I interpret anything.

## Why bias and RMSE?

On a trace, the bias tells you the side of the error, too warm or too cold. The root mean square error tells you the size. And there is a neat identity you can derive on the board. RMSE squared equals bias squared plus the variance of the error. So it separates an offset from a wrong shape.

## Two physics checks

Why is the flow laminar? The jet enters at 0.02 metres per second through five millimetres, so the Reynolds number is about 99, far below transition. And the Richardson number is 1.84: buoyancy is slightly stronger than inertia, so the jet bends upwards within a few inlet widths.

Why the Boussinesq approximation? The density changes only a little over this temperature range. So we keep it constant everywhere, except in the gravity term. And here is the nice link to the thesis: that buoyancy term is exactly the link the replay cuts.

## What would you do differently? Future work

Three things. Let the recorded diffusivity act, with an implicit exchange or a shorter time step. Split the conservation constraint into compartments, so it does not push heat back to the front. And use several recordings, chosen by the state of the replayed temperature, so that more than one regime is covered.

## Which papers influenced you most?

Lichtenegger and Pirker, 2016, which introduced recurrence CFD and the recurrence matrix. Pirker and colleagues, 2018, for the face exchange and the conservation constraint. And Zalesak, 1979, for the local bounds of flux-corrected transport that my limiter uses.

## Three things to remember

One. Under the cold lid, the heat content is right, but the layers separate too slowly: that is missing transport.

Two. A recorded flux reduces the lag from 2.25 to 0.45 kelvin, but the tank then ends 0.86 kelvin too cold.

Three. I know I am right because replays are deterministic, one change per run, the same clock on both sides, and a closed energy budget.

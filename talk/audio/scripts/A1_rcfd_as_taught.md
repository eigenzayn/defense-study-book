# A1 · Recurrence CFD, as Professor Pirker teaches it

Professor Pirker is your supervisor, and he taught Numerical Methods in Fluid Mechanics. Expect him to stay close to recurrence CFD and to the figures of your thesis. In this episode, we go through recurrence CFD the way his lecture tells it, so that your answers sound like his course, and then we link every idea to your own work.

## Why recurrence CFD at all?

Start with the big picture. Many industrial flows run for a long time, and they show recurring patterns. Think of bubble columns, fluidized beds, or turbulent stirred vessels. Solving momentum and pressure for all that time is wasteful, once the flow keeps repeating itself.

So recurrence CFD makes a bold prediction: reuse the recorded flow. And then it corrects that prediction with physics, wherever the reuse breaks something, for example the mass balance.

Here is a lovely way to connect it to the lecture. The SIMPLE algorithm does the same thing. It guesses a pressure, solves the velocity, and then corrects the pressure from continuity. Recurrence CFD guesses the flow from the recording, and then corrects it. Bold prediction, then physics-based correction. If you say that sentence, you are speaking his language.

## Flow-based versus transport-based

There are two families. Flow-based recurrence CFD, from Lichtenegger and Pirker in 2016, stitches recorded flow sequences into a long artificial flow, and it still solves a transport equation on top. That is about 100 times faster than full CFD.

Transport-based recurrence CFD, from Pirker and Lichtenegger in 2018, goes further. It solves no transport equation at all. It replaces it by cell shifts and face swaps. The lecture example is a steel ladle: 26 hours of full CFD, against 1.6 seconds of transport-based recurrence CFD.

Your thesis uses the transport-based form, plus a correction hook and the conservation constraint.

## The recurrence norm, matrix, plateau and prominence

The recurrence norm measures how different two recorded states are. Compute it for all pairs, normalise it, and you get the recurrence matrix.

Now take one row of that matrix. It starts at zero on the diagonal, because a state is identical to itself. Then it rises, and oscillates around a plateau. If the row dips deep below the plateau, the flow comes back to a state similar to an earlier one. That is recurrence, and the replay can jump there. The prominence measures how deep those dips are, relative to the plateau.

The method asks for a prominence of about 0.05 to 0.1. Your tank has a median of 0.028. So the dips are shallow, and the replay plays the frames in order. Say it plainly: my flow is not recurrent, and that is fine, because the saving comes from not solving velocity and pressure.

## The three bold failures

The lecture names three bold failures of recurrence CFD, each with its correction. Learn them as a list of three pairs.

First, mass imbalance. Cell shifts do not conserve mass locally. So a global monitor corrects the total, with mass-acting face swaps.

Second, unphysical diffusion. A fixed number of swaps gives the same mixing everywhere. So the swaps should follow the local mixing.

Third, too little recurrence. In large domains, frames that match globally do not match locally. So the domain is split into recurrence islands, each with its own matrix.

And your thesis touches all three. The conservation constraint is the first. The recorded diffusivity is the second. And your flow, with too little prominence, is the third.

## When does it work, and when does it fail?

It works when the motion repeats, and when the scalar does not change the flow. It fails when the scalar drives the flow, or when the operating state changes. In a new state, the recording simply does not contain the motion that this state would produce.

That is your result. Under the cooled lid, the flow keeps renewing itself with cold plumes, a motion that the insulated recording never saw. And the lecture's answer is multi-state recurrence CFD: one database per process state.

## Digital twins

Professor Pirker likes the digital-twin story. A tank model with one mean value is instant, but it ignores the inside of the plant. Full CFD shows the inside, but takes days. The lecture example: the tank model under one second, the experiment 750 seconds, CFD two days, and recurrence CFD 30 seconds. So recurrence CFD sits in between.

But run blindly forward, it collects error. So live data should keep aligning it. And your thesis shows what such a twin must watch: a boundary condition can move the process into a regime that the database does not cover.

## Is recurrence CFD machine learning?

Here is a careful answer. It is data-based simulation. An expensive ground truth makes the data, a cheap model reuses it, and the real question is how far it generalizes. There is no gradient training. Choosing the next frame is a nearest-neighbour search. And the replay is a sequence of sparse linear operators, close to a learned propagator.

Possible AI steps: learn the map for unseen states, learn the missing flux as a function of the state, or train a neural operator on the database.

## Three things to remember

One. Bold prediction plus physics-based correction, just like SIMPLE guesses a pressure and corrects it.

Two. Three bold failures: mass imbalance, fixed by a global balance; unphysical diffusion, fixed by local swaps; too little recurrence, fixed by islands. Your thesis touches all three.

Three. A database belongs to a flow regime. The lecture's answer is multi-state recurrence CFD, and your cooled lid is the example.

# T2 · Inside the replay: the knob, the drain, and the limiter

This episode is about the heart of the thesis: why the standard replay goes wrong, and how the correction fixes it. If you can tell this story clearly, you can answer most questions about chapters four and five.

## Is the flow recurrent?

Let's start with a question Professor Pirker may ask: is your flow actually recurrent? The honest answer is no.

The recurrence matrix compares every pair of recorded states. A small distance means two states look alike, so the replay could jump from one to the other. In my tank, the matrix shows two blocks: filling and settling. And no state ever comes back. The method asks for a prominence of about 0.05 to 0.1. My tank has a median of 0.028. So the replay simply plays the frames in order.

Is it still recurrence CFD, then? Yes. The saving does not come from jumping between frames. It comes from never solving velocity and pressure again.

## The face exchange, and the knob

A pure displacement does not mix anything. So after each move, the replay library swaps a share of heat across every face, from the warm cell to the cold one. The strength of this swap per step is called f s d. It has no unit, so it is not a diffusion coefficient, but you can translate it into one.

Here is the key property. The exchange can only reduce differences. It can never rebuild a front that has already been smeared.

## No single best setting

I ran seven strengths. The heat content of the tank is best with no added mixing: the error of the mean temperature is 1.07 kelvin. The height of the warm layer is best near one half: an error of only 0.068 millimetres. So no single value is best for both. And with the strongest mixing, the tank ends 5.08 kelvin too cold.

Why does more mixing lose heat? Picture a bathtub with the drain placed just below the warm surface layer. If the layer stays thin, the drain takes cold water. If you smear the layer downwards, warm water reaches the drain and leaves. In my tank, the outlet sits just below the front. So a smeared front turns into a heat leak.

I showed this with the energy balance of the whole tank. Energy in minus energy out gives the outlet temperature. During the warm inflow, the standard replay keeps about 2.7 kelvin too much. After the inflow, it drains 4.6 kelvin through the outlet.

And who smears the front? I checked. With the recorded maps alone, the front at 240 seconds is 2.5 millimetres. With the standard exchange, 19.3. The reference has 4.5. So the maps are fine. The exchange is guilty.

## Why not just use negative diffusion?

This is a classic examiner question. Diffusion smooths. So why not run it backwards to sharpen the front?

Because negative diffusion is ill-posed. It amplifies every disturbance, and the shortest wiggles grow fastest. You can show it with one Fourier mode. For the explicit diffusion step, the growth factor is one minus four nu times sine squared of k delta x over two. For a negative nu and the shortest mode, the factor is one plus four times the absolute value of nu. That is larger than one, so the wiggle grows at every step. In my one-dimensional test, after 21 steps, the field left the range of the data.

So I keep the useful part, the steepening, and I stop the dangerous part with a limiter.

## The limiter

For every cell, take the smallest and the largest value among the cell and its neighbours. Those are its local bounds. The headroom of the warm cell is how far it can still rise. The headroom of the cold cell is how far it can still fall. Across a face, heat moves uphill, from the colder cell to the warmer one, and the amount is the smaller of the two headrooms, times a strength s.

So no cell can leave its bounds. A maximum cannot grow, a minimum cannot sink. And the heat that leaves one cell enters the other, so energy is conserved face by face. This is the limiter idea of flux-corrected transport, from Boris and Book, and from Zalesak.

There is also a neat bound. A hexahedral cell has six faces. If s is at most one sixth, no cell can leave its bounds even before any clamp acts. My working range, 0.40 to 0.50, is above that, so it relies on the clamp and on the global conservation constraint. Say that honestly if they ask.

## Why the vertical weight?

The front is horizontal. So the correction should act across it, not along it. Each face gets the weight cosine squared of the angle between its link and the vertical. Faces across the front get one, faces along it get zero. Without the weight, the correction roughens the front sideways. Mathematically, this weight is exactly the face coefficient of a diffusion that acts in one direction only.

## The recorded diffusivity did not help

One more result you must be able to explain. I also tried a recorded, local diffusivity instead of the constant knob. It changed nothing, and the replays were bit-identical. Why? The recorded values ask for more exchange than the explicit step can apply. Every face hits the cap, so the field behaves exactly like the constant setting. A shorter time step or an implicit exchange would let it act.

## The result

With the correction, the end front goes from 15.7 millimetres to between 5.3 and 4.5. The reference has 5.0. The error of the mean temperature over the run drops from 1.46 to about 0.7 kelvin. And remember the honest sentence: the strength was chosen against the same reference.

## Three things to remember

One. No single knob setting works, because the outlet below the front drains the heat of a smeared front.

Two. Negative diffusion grows wiggles. The limiter keeps the steepening and stays inside the neighbours' bounds, so no new extremes and no lost heat.

Three. 15.7 millimetres becomes about 5, the reference is 5.0, and the strength was chosen with the reference.

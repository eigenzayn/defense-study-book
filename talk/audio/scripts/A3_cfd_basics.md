# A3 · The CFD basics behind recurrence CFD

This last episode covers the CFD basics from Professor Pirker's lecture. These are the questions that test whether you really understand the ground that recurrence CFD stands on. The trick for each one is the same: say the idea, give one formula, and connect it to your thesis. That connection is what turns a textbook answer into your answer.

## Dimensionless numbers

The Reynolds number compares inertia with viscous forces: U times L over nu. Pipe flow is laminar below about 2300, and turbulent above about 4000.

A few others. The Péclet number compares convection with diffusion. The Prandtl number compares momentum diffusion with heat diffusion. The Froude number compares inertia with gravity. And the Richardson number compares buoyancy with inertia.

Your case: a Reynolds number of about 99, so laminar, and a Richardson number of 1.84, so buoyancy is a little stronger than inertia.

## Governing equations and the material derivative

Mass, momentum and energy are conserved. There are two ways to look at a flow. The Lagrangian view follows a fluid parcel. The Eulerian view watches a fixed point.

The material derivative links them. It is the rate of change seen by the moving parcel: the local change in time, plus the velocity dotted with the gradient. You get it from the chain rule along the path, because the parcel moves with the velocity.

Momentum, in words: the change in time plus the convection equals the pressure force, plus the viscous force, plus the body force.

## The finite-volume method

Integrate the equation over each cell. The divergence theorem turns every divergence into fluxes through the faces. And what leaves one cell enters its neighbour, so the method is conservative.

Each cell value is then linked to its neighbours by one linear equation: a P times c P equals the sum of the neighbour coefficients times the neighbour values, plus a source. That is the computational molecule.

Here is the connection to your thesis. If all coefficients are positive, the new value is a weighted mean of its neighbours, so no new extremum can appear. That is exactly the rule that protects the face exchange in recurrence CFD, and the same idea behind your limiter.

## Discretization schemes and numerical diffusion

First-order upwind takes the value from upstream. It is stable, but it adds false diffusion. Central differencing is more accurate, but it can oscillate when the cell Péclet number is above two.

Why does upwind diffuse? Expand the upstream value in a Taylor series. The upwind difference equals the true derivative minus one half delta x times the second derivative. So the equation that upwind really solves has an extra diffusion term, with a numerical diffusivity of one half times u times delta x.

And this is your thesis in one sentence: it is a numerical-diffusion story. The face exchange smears the front, and the correction undoes it.

## Explicit versus implicit time stepping

Explicit steps are cheap, but limited by stability. Implicit steps solve a system of equations, but are unconditionally stable.

For explicit convection, the Courant number must be below one: information must not travel more than one cell per step. For explicit diffusion, the diffusion number, Gamma delta t over delta x squared, must be below one half.

You can show the diffusion limit on the board. Insert one Fourier mode into the explicit diffusion step. The growth factor is one minus four d times sine squared of k delta x over two. It stays between minus one and one for every mode only if four d is at most two, so d at most one half.

And again, the link: this explicit diffusion limit is exactly the cap that stopped the recorded diffusivity in your replay.

## The SIMPLE algorithm

SIMPLE means Semi-Implicit Method for Pressure-Linked Equations, from Patankar. Four steps. One: guess the pressure, and solve the momentum equation for a velocity. Two: write the velocity correction as a function of the pressure correction. Three: put that into continuity, which gives an equation for the pressure correction. Four: correct both fields, with under-relaxation, and repeat until the residuals are small.

Guess, solve, correct, repeat. And remember from the first episode: recurrence CFD follows the same spirit.

## Turbulence

Turbulence is chaotic, and it mixes strongly. Energy enters at the large eddies and cascades down to the Kolmogorov scale, where viscosity dissipates it.

You can derive the Kolmogorov length from dimensions. It may depend only on the viscosity nu and the dissipation rate epsilon. Match metres and seconds, and you get eta equals nu cubed over epsilon, to the power one quarter.

RANS splits the velocity into a mean and a fluctuation, and models all eddies, usually with an eddy viscosity, like C mu times k squared over epsilon in the k-epsilon model. LES models only the small eddies. DNS models none. And your case needs none of this, because it is laminar.

## Wall boundary layers

Near a wall, the velocity drops to zero. y plus says how far the first cell sits from the wall, in viscous units: the friction velocity times the wall distance, over nu. The viscous sublayer lies below a y plus of about five, the log layer above about thirty. Wall functions put the first cell in the log layer and model the rest, which is cheap. A wall-resolved simulation needs a y plus of about one.

## Heat transport and Boussinesq

Temperature and species follow the same transport equation: change in time plus convection equals diffusion plus a source. If the density depends on temperature, the flow and the temperature are coupled.

For small density changes, the Boussinesq approximation keeps the density constant everywhere, except in the gravity term. And that buoyancy term is the exact link that the replay cuts.

## Multiphase flows

Euler–Euler treats each phase as a continuum, with volume fractions. It suits dense systems at lower cost. Euler–Lagrange tracks every particle, and with particle contacts it becomes CFD–DEM: accurate, but expensive. And recurrence CFD was first used for bubble columns and fluidized beds.

## Three things to remember

One. Finite volumes are conservative, and positive coefficients mean no new extremes: the same rule protects your limiter.

Two. Upwind adds a numerical diffusivity of one half u delta x. Your thesis is a numerical-diffusion story.

Three. Explicit limits: Courant below one, diffusion number below one half. That diffusion limit is the cap that stopped the recorded diffusivity.

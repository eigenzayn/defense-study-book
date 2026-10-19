# A2 · Reading the figures of my thesis

Professor Pirker often points at a figure and asks: what does it show, and why? So for every important figure, you need three sentences ready. What is plotted. What we see. And why it matters. In this episode, we practise exactly that. I will describe each figure by its content, not by its number, because the numbering may still change.

## The passive and the non-passive scalar

The opening figure has three panels. First, a dye in the stored velocity of the insulated tank: it is only stretched by the flow. Second, the cooled tank, where cold plumes from the lid create the motion. Third, the replay, which moves temperature with recorded maps and never solves the velocity.

Why it matters: it is the whole thesis question in one figure. A dye only rides the flow, but temperature makes the flow, and the replay cuts that feedback.

## The recurrence of the database

This figure shows the distance matrix of the recording. It has two blocks, split at the end of the inflow: filling, and settling. The rows rise to a plateau, and none of them returns towards zero.

Why it matters: the prominence, a median of 0.028, stays below what the method needs. So no state comes back, and the replay plays the frames in order.

## Vertical heat transport under the cooled lid

This figure splits the plane-mean vertical heat flux into two parts: the part carried by the flow, and the part carried by conduction. Under the cooled lid, the flow carries far more heat than conduction, and the temperature departures have the size of whole plumes.

Why it matters: cooling is a transport process. A diffusive step cannot copy it.

## The two regimes

Same geometry, same inflow, two different flows. With the insulated lid, the jet rises, spreads under the lid, and the warm layer then rests. With the cooled lid, the layer above the front overturns in a row of cells, driven by cold plumes.

Why it matters: one boundary condition switches the flow from one regime to another.

## The standard replay over the mixing sweep

Two panels: the mean temperature, and the height of the heat, for seven mixing strengths. More mixing heats the tank faster during the inflow, and drains it faster afterwards. The height is best at a medium strength, the heat content with little mixing.

Why it matters: there is no single best setting.

## The insulated tank through the run

The mid-plane temperature at four times, with the front width written in each panel. The replay with the recorded maps alone keeps the front as thin as the reference. The standard replay smears it. The corrected replay makes it thin again.

Why it matters: the smearing comes from the face exchange, not from the maps.

## The space–time diagram

The horizontal mean temperature, plotted against height and time. You see the warm layer growing downwards. The difference panel shows where the standard replay is too warm or too cold, and the thickness panel shows its front stays too thick. The corrected replay follows the reference.

## Every correction run in one map

Each marker is one replay: the trace error and the end-profile error, plotted against the front width. Only the vertically weighted form brings both errors down while the front reaches the reference width of 5.0 millimetres. Its working range is s from 0.40 to 0.50.

Why it matters: direction matters more than strength.

## The buoyancy frequency across the front

The buoyancy frequency says how strongly the layering resists vertical motion. N squared equals g times beta times the vertical temperature gradient. The standard replay holds a barrier only about half as strong as the reference. The corrected replay reaches the reference value after the inflow.

Why it matters: a sharper front is a stronger barrier, so the correction restores the stability of the front, not only its width.

## End profiles through the front

Without correction, the front is wide and too high. The unweighted correction makes it thin, but puts it in the wrong place. The vertical weight follows the reference.

Why it matters: a saw-toothed front can have the right width and the wrong shape. Always read the width together with the profile.

## The outlet temperature from the energy balance

The outlet temperature is recovered from the energy balance of the whole tank: the mass times the rate of change of the mean temperature equals the mass flow times inlet minus outlet temperature. While the inflow is warm, the standard replay keeps about 2.7 kelvin too much heat. Afterwards, it drains 4.6 kelvin.

Why it matters: the outlet sits just below the front, so a numerical error at the front becomes an error in the energy budget.

## The state space

The two leading POD modes of the reference field, and the distance of each run from the space of the first ten modes. The standard replay leaves this space and does not return. The corrected replay comes back after the inflow.

Why it matters: the correction keeps the replay close to the states that the recording spans.

## The cooled lid: profiles, traces, and plumes

The end profiles: the standard replay holds nearly the right heat, but in the wrong place, with a profile error of 2.79 kelvin. The bulk is too warm, the top layer too cold. The correction moves the heat back.

The traces: a shaded band shows how far the local correction lags in heterogeneity during the warm inflow. Only the recorded flux also follows the heterogeneity. A lag in layering is missing transport, not missing sharpness.

And in 3D: the plumes of the standard replay end halfway down. With the correction, they reach the front again. The replay invents no motion. The plumes were in the recorded maps all along.

## The recurrence of the two recordings

After the inflow, the cooled flow keeps renewing itself, about ten times faster at short lags, while the insulated flow hardly changes.

Why it matters: the cooled case is a different regime, so a database recorded without cooling cannot contain its motion.

## Three things to remember

One. For every figure: what is plotted, what we see, why it matters.

Two. The key chain of figures: no single mixing setting, the maps keep the front thin, the outlet drains heat, the vertical correction restores width and stability.

Three. Under the cooled lid: right heat, wrong place without correction; the lag is missing transport; and a different regime needs a different database.

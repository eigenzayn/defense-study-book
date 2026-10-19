# T1 · My thesis in plain words

Here is a question you will almost certainly hear on the day: what problem did you solve? So let's practise the answer, slowly, until it feels like your own story.

Start with the method. Recurrence CFD is a way to make simulation cheap. You run one normal, full simulation. While it runs, you record, frame by frame, which share of each cell moves to which other cell. After that, you never solve the velocity or the pressure again. You simply replay the stored motion, and you use it to carry something through the tank. That is why it is fast. In my case, the full simulation took 569 minutes of solver time. One replay took about two minutes. That is roughly 260 times faster.

Now, here is the catch. The method was built for passive scalars. A passive scalar is something that rides along with the flow but does not change it, like a dye. Temperature is not like that. Warm water is lighter, so it rises. Temperature drives the flow by buoyancy. So when the replay keeps the recorded motion fixed, it cuts that feedback.

So the answer to "what problem did you solve?" is this. I tested recurrence CFD on temperature, a scalar that drives its own flow. I measured what the replay loses, and how much I can repair without solving the flow again.

## Why should anybody care?

The second question is often: why should I care? Here is a short, honest answer. Thermal processes run for hours, and full CFD of that time is too slow for daily use. A replay that is 260 times faster sounds wonderful. But a fast model is only useful if you know its error. My thesis measures that error, for a case where temperature matters, and it shows which part of the error can be repaired.

Fast is useful only with a known error. Say that sentence slowly. It is a good line.

## Recurrence CFD in simple words

If they ask you to explain recurrence CFD simply, use the traffic camera. Imagine a camera that records the route of every car in a city. Next time, you do not simulate the drivers. You reuse the recorded routes to move parcels around. That is the replay.

But every analogy has a limit, and examiners love the limit. Here it is: the recording does not store pictures. It stores maps of how much fluid goes from cell to cell. And if the parcels are heavy enough to change the traffic, the old routes are wrong. That is temperature.

One replay step has four stages. Remember them as map, swap, correct, balance. Map: the recorded map moves the heat. Swap: a face exchange adds a little mixing between neighbours. Correct: this is my contribution, the correction stage. Balance: a conservation constraint fixes the total heat. In standard recurrence CFD, the correction stage does nothing. In my thesis, it does the real work.

## Why is this AI, and not only CFD?

This question came up in earlier defenses, so be ready. Recurrence CFD is a data-based simulation. An expensive solver produces data, and a cheap model reuses it. The database of recorded states plays the role of training data. Choosing the next frame is a nearest-neighbour search in that database, which is the old method of analogues.

And my main finding is really a finding about generalization. A database belongs to a flow regime. If a boundary condition changes the regime, the database is out of distribution. In machine learning words: the test data no longer looks like the training data. That is exactly what happens when the lid of my tank gets cold.

## The test case

You should be able to describe the tank without notes. A closed tank, seventy-five by seventy-five by fifteen millimetres, with one-millimetre cells. A warm jet enters at mid-height, at 333 kelvin and 0.02 metres per second, for 315 seconds. The Reynolds number is about 99, so the flow is laminar. And there are two versions of the lid: an insulated one, and a cooled one.

## Three things to remember

One. The problem: recurrence CFD was built for a dye, and I tested it on temperature, which pushes back on the flow.

Two. The value: 260 times faster, but fast is useful only with a known error, and I measure that error.

Three. The AI view: the database is training data, and a new flow regime means the data is out of distribution.

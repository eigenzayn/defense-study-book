# M2 · From one neuron to backpropagation

This is the most asked topic in the whole exam. Professor Hochreiter, Professor Klambauer and others have asked it again and again: explain backpropagation and define the delta error. Your goal is simple. You should be able to write it on the board in two minutes, and explain every line while you write. Let's get there.

## One neuron

A neuron takes a weighted sum of its inputs, adds a bias, and passes the result through a non-linear function. The weighted sum is called the pre-activation, s. The result, a equals f of s, is the activation. A layer does this for many neurons at once, so in matrix form, the activation of layer l is f of W times the activation of the layer below, plus b. The forward pass goes layer by layer, from the input to the output.

## Why do we need the non-linearity?

Professor Schlüter has asked: what happens without activation functions? The whole network collapses into one linear model. Multiply two linear maps, and you get another linear map. So depth adds nothing, and the network cannot even solve XOR. The non-linearity is what makes depth useful.

## The universal approximation theorem

One hidden layer, with enough units and a non-polynomial activation such as a sigmoid, can approximate any continuous function on a compact set. Now the important part, the limit. The theorem says the network can represent the function. It does not say how many units you need. And it does not say that gradient descent will find the weights. Existence, not learnability.

## Backpropagation: the idea

Here is the problem. A network may have millions of weights, and we need the gradient of the loss for every single one. Doing that one by one would be hopeless.

Backpropagation gets all of them with one forward pass and one backward pass. Think of it like tracing blame in a team. The output is wrong by some amount. Each unit gets a share of the blame, depending on how much it contributed. And that blame flows backwards, layer by layer. That share of blame is the delta.

## The delta, defined

Write this first: delta i is defined as the derivative of the loss with respect to the pre-activation s i.

Now the gradient of a weight w i j. The weight acts on the loss only through s i. So by the chain rule, the derivative of the loss with respect to w i j equals delta i, times the derivative of s i with respect to w i j. And because s i is the weighted sum, that derivative is just a j.

So the gradient is delta i times a j. In words: the delta of the unit above, times the activation of the unit below. That is the line examiners want to hear.

And the update: w i j becomes w i j minus eta, times delta i, times a j.

## The recursion

Next question: how do we get the deltas of hidden units? A hidden unit j affects the loss only through the units i in the next layer. So we sum over those paths.

Delta j equals the sum over i of delta i, times w i j, times f prime of s j.

In matrix form: take the deltas of the layer above, multiply by the weight matrix transposed, then multiply element by element by the slopes of the activations. Deltas flow down: multiply by W transposed, then by f prime.

And the gradient for a whole weight matrix is the outer product: the delta vector of layer l times the activation vector of the layer below, transposed. The cost is linear in the number of weights. That is why backprop is efficient.

## The delta at the output

Professor Hochreiter likes this one: what is the delta at the output with softmax and cross-entropy? The answer is beautifully simple. Prediction minus label.

You can derive it. The derivative of the softmax output a k with respect to s i is a k times, one if k equals i minus a i. Put that into the derivative of the cross-entropy, use the fact that a one-hot label sums to one, and everything collapses to a i minus y i.

The same clean result holds for a linear output with squared loss, and for a sigmoid with binary cross-entropy. That is why these pairs are used together.

## Vanishing and exploding gradients

Now look at the recursion again. To get the delta of the first layer, you multiply by one Jacobian per layer. So over many layers, the delta shrinks or grows exponentially. With the sigmoid, the slope is at most one quarter. If one quarter times the weight norm is below one, the delta vanishes as the network gets deeper.

And here is the Linz connection: Sepp Hochreiter analysed this problem in his diploma thesis in 1991, here in Linz. If the examiner asks who found it, that is your answer, and it is a good moment to smile.

The fixes: ReLU or SELU activations, good initialization, normalization, residual connections, and for sequences, the LSTM.

## Three things to remember

One. Delta is the derivative of the loss with respect to the pre-activation. The gradient is the delta above times the activation below.

Two. Deltas flow down: multiply by W transposed, then by f prime. At the output, softmax with cross-entropy gives prediction minus label.

Three. A product of Jacobians vanishes or explodes. Hochreiter, 1991, Linz. Fixes: ReLU or SELU, initialization, ResNet, LSTM.

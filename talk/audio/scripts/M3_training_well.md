# M3 · Training well: optimizers, activations, regularization

Once you have gradients, you have to use them well. This episode covers the short questions that come after backpropagation: gradient descent, optimizers, activation functions, regularization and initialization. They are quick questions, so your answers should be quick too. One clear sentence, then one detail.

## Gradient descent and mini-batches

Gradient descent moves the weights a small step against the gradient of the empirical risk. The weights become the weights minus eta, times the gradient. Eta is the learning rate.

Why mini-batches? Think of a hiker in fog, trying to walk downhill. The full batch is like surveying the whole mountain before every step: exact, but slow. One sample is like guessing from one stone under your foot: cheap, but noisy. A mini-batch is the compromise. It gives an unbiased estimate of the gradient, it runs fast and in parallel on a GPU, and its small noise even helps the weights escape sharp minima.

## Which optimizers do you know?

Gradient descent, stochastic gradient descent, momentum, AdaGrad, RMSprop and Adam.

Momentum keeps a running sum of past gradients, like a ball rolling downhill that keeps its speed through small bumps. AdaGrad and RMSprop give each weight its own step size, based on its past squared gradients. Adam combines both ideas, momentum and RMSprop, with a bias correction for the first steps. It is the usual default.

## Other training methods

Professor Klambauer has asked: are there methods other than gradient descent? Yes. Linear models have a closed form. Logistic regression can use iteratively reweighted least squares. RProp and Quickprop use only the sign or the curvature of the gradient. Newton, Gauss–Newton, Levenberg–Marquardt and conjugate gradients use second-order information. And evolutionary algorithms or random search need no gradient at all.

## Activation functions, and the one from Linz

This is a favourite question of Professor Hochreiter: which activation functions do you know, and which one is from Linz?

Sigmoid and tanh are smooth, but they saturate, so their gradients become tiny. ReLU is cheap and does not saturate for positive inputs, but units can die: if a unit's input stays negative, it never learns again.

And from Linz: ELU and SELU, developed at JKU. SELU, from Klambauer and colleagues in 2017, makes a network self-normalizing. The mean and the variance of the activations are pulled towards zero and one, layer after layer, without any extra normalization layer. The constants: lambda is about 1.0507, and alpha is about 1.6733. The fixed point is zero mean and unit variance.

For the output layer: linear for regression, sigmoid for two classes, softmax for many classes.

## Regularization

Weight decay, dropout, early stopping, data augmentation and noise.

Weight decay adds a penalty, lambda over two times the squared norm of the weights. Its gradient adds lambda times w, so in every step the weights shrink by a factor of one minus eta lambda before the normal update. That is where the name comes from.

Dropout switches units off at random during training, so the network cannot rely on any single unit. Think of a team where any member may be absent on a given day: everyone has to learn the job. Early stopping ends training when the validation error starts to rise.

## Initialization and batch normalization

Why does initialization matter? Two reasons. First, random weights break the symmetry. If all weights start equal, all units learn the same thing. Second, the scale. If it is wrong, the signal and the deltas vanish or explode through the layers.

Here is the short derivation. A pre-activation is a sum over n in inputs of weight times activation. With independent, zero-mean weights, its variance is n in, times the variance of the weights, times the mean square of the activations. To keep the variance constant, choose the weight variance as one over n in. For ReLU, which halves the mean square, choose two over n in. That is He initialization.

Batch normalization standardizes each pre-activation over the mini-batch, and then rescales and shifts it with learned parameters.

## Three things to remember

One. Mini-batches: a cheap, unbiased, parallel gradient estimate, with useful noise. Adam is momentum plus RMSprop with bias correction.

Two. The Linz activations are ELU and SELU. SELU is self-normalizing, with lambda about 1.0507 and alpha about 1.6733.

Three. Initialization keeps the variance constant: one over n in, or two over n in for ReLU. Regularization: weight decay, dropout, early stopping, augmentation, noise.

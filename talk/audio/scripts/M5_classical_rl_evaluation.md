# M5 · Classical machine learning, REINFORCE, and evaluating a model

The last ML&P episode covers the questions that sit next to deep learning: the support vector machine, kernels, the VC dimension, the REINFORCE loss, and how to evaluate and stress-test a classifier. Some of these were asked by Professor Kofler and Professor Hochreiter, so they are worth your time.

## The support vector machine

The idea in one sentence: the SVM finds the separating hyperplane with the largest margin.

Picture a road between two groups of houses. The SVM builds the widest possible road, and the houses that touch the edge of the road are the support vectors. Only they decide where the road goes.

The margin is two over the norm of w. So maximizing the margin means minimizing the norm of w, squared. In the soft-margin version, some points may sit inside the margin. We allow that with slack variables, and we pay for it with a penalty C. So we minimise one half the squared norm of w, plus C times the sum of the slacks, subject to each point being on the right side, up to its slack.

In the dual problem, only dot products between data points appear. The points with alpha n greater than zero are the support vectors.

## Kernels and the kernel trick

A kernel is a dot product in a feature space, computed without building the features.

Here is the classic example. Take the polynomial kernel in two dimensions: x transposed x prime, squared. Multiply it out, and you get exactly the dot product of two feature vectors, with features x one squared, root two times x one x two, and x two squared. So the kernel computed the dot product in that three-dimensional feature space, without ever constructing it.

And since the SVM dual needs only dot products, we can replace them by a kernel. That gives a non-linear classifier at the cost of a linear one. Examples: the polynomial kernel and the Gaussian kernel.

## The VC dimension

The VC dimension is the largest number of points that a model class can label in every possible way. We say the class can shatter that set. It measures capacity. For linear classifiers in d dimensions, the VC dimension is d plus one. In generalization bounds, the gap between training and test error grows with the VC dimension and shrinks with the number of samples.

## REINFORCE, asked by Professor Hochreiter

We want the policy with the largest expected return. The expected return J of theta is the integral over trajectories of the probability of a trajectory, times its return.

The trick is the log-derivative trick: the gradient of p equals p times the gradient of log p. That moves the gradient inside the expectation, so we can estimate it from sampled episodes.

Now write the log-probability of a trajectory. It is the log of the start state, plus the sum over time of the log-policy, plus the log of the environment dynamics. The environment does not depend on the policy parameters. So when we take the gradient, only the policy terms survive.

The result: the gradient of J is the expected value of the sum over time of the gradient of log pi of a t given s t, times the return G t. As a loss to minimise, we write minus the sum of log pi of the action, times the return minus a baseline. The baseline does not change the expected gradient, but it reduces the variance.

## How do you evaluate a classifier?

With the confusion matrix, precision, recall and the area under the ROC curve.

Precision: of everything I called positive, how much is right? True positives over true positives plus false positives. Recall: of all real positives, how many did I find? True positives over true positives plus false negatives. A simple way to remember: precision is how clean, recall is how complete.

The ROC curve plots the true-positive rate against the false-positive rate, over all thresholds. The AUC is the probability that a random positive gets a higher score than a random negative. An AUC of 0.5 is chance. An AUC of one is perfect.

## How else can you measure robustness?

Professor Klambauer has asked: besides adversarial attacks, how else can you measure robustness? Test under distribution shift: corrupted inputs, new domains, data from another time. Check calibration and uncertainty, with ensembles or Monte Carlo dropout. And check how sensitive the output is to small changes of the input.

And here you can bring in your own thesis. A recording made under one boundary condition fails under another, because the regime changed. That is distribution shift, in a physics simulation. It is a strong, personal answer.

## Three things to remember

One. SVM: maximum margin; the dual has only dot products, so a kernel gives a non-linear classifier at linear cost. Linear classifiers in d dimensions have VC dimension d plus one.

Two. REINFORCE: the log-derivative trick, the dynamics drop out, and the loss is minus log pi times the return minus a baseline.

Three. Precision is how clean, recall is how complete, AUC is ranking quality. Robustness: distribution shift, calibration, sensitivity, and your own regime example.

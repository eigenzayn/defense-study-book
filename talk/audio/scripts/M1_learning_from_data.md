# M1 · Learning from data: risk, loss, and the bias–variance story

Almost every Machine Learning and Perception exam starts in the same place. The examiner says: write down a supervised data set and the training framework. If you can tell this story calmly, the rest of the exam gets easier. So let's build it, piece by piece.

## Data, model, loss, average, minimise

We have N pairs. Each pair is an input x n and a label y n. We assume the pairs are drawn independently from one unknown distribution, p of x and y.

A model g maps an input to a prediction, and it has weights w. A loss L says how wrong one prediction is. If we average the loss over all training pairs, we get the empirical risk. And learning simply means: find the weights that minimise the empirical risk.

Remember it as five words: data, model, loss, average, minimise.

## Why not minimise the real error?

The examiner will push: what is the generalization error, and why can't we minimise it directly?

The generalization error is the expected loss on new data, drawn from the true distribution. To compute it, you would need to integrate the loss against p of x and y. But p is unknown. That is the whole problem of learning.

So we minimise the empirical risk instead, and we estimate the generalization error on data we did not train on: a test set, or cross-validation. By the law of large numbers, the average loss on a large test set approaches the expected loss.

And one trap to avoid: the training loss is not a fair estimate. The weights were chosen on that data, so it looks too good.

## What is a loss function?

A loss compares a label with a prediction. It is never negative, and it is zero when the prediction is right. You pick it for the task.

For regression, the squared loss: one half times the label minus the prediction, squared. For two classes, binary cross-entropy. For many classes, categorical cross-entropy: minus the sum over classes of the label times the log of the predicted probability. And for the support vector machine, the hinge loss.

Professor Klambauer has asked a nice follow-up: are all losses differentiable? No. The zero-one loss, which just counts mistakes, has no useful gradient. It is flat almost everywhere. So for training we use cross-entropy instead.

## Linear regression as the warm-up

With a linear model and the squared loss, the risk is a bowl. It is convex, so there is one minimum, and you can find it in closed form. Take the gradient of one half times the squared norm of y minus X w. It is minus X transposed times the error. Set it to zero, and you get the normal equations. The solution is X transposed X, inverted, times X transposed y. That is the pseudo-inverse.

Notice one pattern here, because it comes back in backpropagation. For one sample, the gradient is the error times the input.

## Overfitting, underfitting, bias and variance

Here is a picture that helps. Imagine shooting arrows at a target, many times, each time with a new training set. Bias is how far the centre of your arrows is from the bullseye. Variance is how widely your arrows scatter.

A model that is too simple has high bias. It cannot follow the data, so it underfits. A model that is too complex has high variance. It follows the noise in each training set, so the training error is low, but the test error is high. That is overfitting.

The formula behind the picture: the expected squared error equals noise, plus bias squared, plus variance. You derive it by adding and subtracting the average model prediction. The cross terms have zero mean, so they disappear.

And the modern twist: very large networks show double descent. After the point where they fit the training data exactly, the test error falls again. Mention it in one sentence. It shows you know the classic curve is not the whole story.

## Maximum likelihood

Professor Widmer has asked this one several times. Maximum likelihood chooses the parameters that make the observed data most probable. We maximise the log-likelihood, because a sum is easier than a product.

The neat connection: squared loss is maximum likelihood under Gaussian noise. Write the likelihood of a Gaussian, take minus the log, and the only part that depends on the weights is the sum of squared errors.

And the weakness: with little data, maximum likelihood overfits. An event you have never seen gets probability zero. A prior, which gives you MAP estimation, or regularization, fixes that.

## Three things to remember

One. Data, model, loss, average, minimise: that is empirical risk minimization.

Two. The generalization error needs the unknown distribution, so we estimate it on a test set or by cross-validation, never on the training data.

Three. Simple models have bias, complex models have variance, and very large nets show double descent.

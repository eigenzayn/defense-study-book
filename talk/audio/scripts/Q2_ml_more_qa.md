# Q2 · Questions and answers: Machine Learning, the other asked questions

This track covers the other machine learning questions that were asked in past defenses: losses, likelihood, the SVM dual, the VC dimension, EM, attention, the LSTM, REINFORCE and evaluation. The format is the same as before. A question, a pause for your own answer, one sentence to learn by heart, and then the derivation, step by step.

## 1 · Name loss functions and their properties

Question 1. Name loss functions and their properties.

Squared loss for regression, cross-entropy for classification, hinge loss for the SVM, and the zero-one loss, which counts errors but has no useful gradient.

Where does cross-entropy come from? Treat the softmax output as a probability distribution over classes. The probability of the correct label is the product over k of a k to the power y k, because the one-hot label picks exactly one factor. Take minus the log. The product becomes a sum, and we get minus the sum over k of y k times log a k. So cross-entropy is just the negative log-likelihood of the label.

The hinge loss is the maximum of zero and one minus y times f of x. It is zero for points that are on the right side with a margin of at least one, and it grows linearly for the rest. The zero-one loss is what we really care about, but it is flat almost everywhere, so its gradient is zero. That is why we train with a smooth surrogate. Squared loss punishes large errors strongly, so it is sensitive to outliers. Absolute loss is robust, but not smooth at zero.

## 2 · State the universal approximation theorem

Question 2. State the universal approximation theorem.

One hidden layer with a non-polynomial activation and enough units can approximate any continuous function on a compact set as closely as we want.

Here is the idea behind the proof, in three steps. First, a sigmoid with a very large weight becomes almost a step, so one unit can switch on at any position we choose. Second, two such steps with opposite signs make a bump: up at one position, down at the next. Third, a weighted sum of many narrow bumps can follow any continuous curve, just like the bars of a histogram. More units give narrower bumps and a better fit. Cybenko showed it in 1989 and Hornik in 1991. Now the limit, which examiners like to hear. The theorem says that such a network exists. It does not say how many units we need, and it does not say that gradient descent will find the weights. Existence, not learnability. In practice, deep networks often need far fewer units than one wide layer.

## 3 · Are there training methods other than gradient descent?

Question 3. Are there training methods other than gradient descent?

Yes: closed-form solutions, second-order methods like Newton or L-BFGS, EM, coordinate descent, and gradient-free methods such as evolutionary search.

Let us derive the Newton step. Gradient descent uses only the slope. Newton also uses the curvature. Write the loss near w with a second-order Taylor expansion: L of w plus delta, is about L of w, plus g transpose delta, plus one half delta transpose H delta. Here g is the gradient and H is the Hessian. Set the derivative with respect to delta to zero. That gives g plus H delta equals zero, so delta equals minus the inverse of H, times g. For a quadratic loss this lands on the minimum in one step. The price is the Hessian, which is huge for a network, so L-BFGS builds a cheap approximation from past gradients. For linear regression we do not need iterations at all. The normal equations give the solution in closed form. And when the loss is not differentiable, evolutionary strategies or random search need no gradient at all.

## 4 · Which output activation and loss for regression and for classification?

Question 4. Which output activation and loss for regression and for classification?

Regression uses a linear output with squared loss, and classification uses softmax with cross-entropy, or a sigmoid with binary cross-entropy for two classes.

Both pairs come from maximum likelihood. For regression, assume the target is the prediction plus Gaussian noise. The density is proportional to e to the minus, y minus y hat squared, over two sigma squared. Take minus the log. What remains is y minus y hat, squared, over two sigma squared, plus a constant. So minimising the squared loss is maximum likelihood under Gaussian noise. For two classes, assume a Bernoulli label with probability a. The likelihood is a to the y, times one minus a, to the one minus y. Minus the log is exactly binary cross-entropy. For many classes, the same step with a categorical distribution gives softmax cross-entropy. And all three pairs give the same clean output delta, prediction minus label.

## 5 · How can you do feature selection?

Question 5. How can you do feature selection?

Filter methods rank features by a statistic, wrapper methods search subsets with the model, and embedded methods select features during training, for example with L1.

Filters are fast. They score each feature on its own, for example with the correlation or the mutual information with the target. Wrappers, like forward selection, add one feature at a time and keep it if the validation score improves. They are accurate but expensive, because they train the model many times. Embedded methods select while training. Why does L1 give exact zeros? Its gradient is lambda times the sign of w. This push has the same size no matter how small the weight is, so it drives small weights all the way to zero. The L2 gradient, lambda times w, becomes tiny near zero, so it only shrinks. One warning: always select inside the cross-validation loop, otherwise the test data leak into the choice.

## 6 · The SVM dual and the kernel trick

Question 6. Write down the SVM and explain kernels and the kernel trick.

The SVM maximises the margin, and in its dual form the data appear only through dot products, so a kernel can replace them and compute a dot product in a feature space without building it.

Let us derive the dual. The primal is: minimise one half the squared norm of w, subject to y i times, w transpose x i plus b, at least one. Add a Lagrange multiplier alpha i, at least zero, for each constraint. The Lagrangian is one half the squared norm of w, minus the sum over i of alpha i, times, y i times w transpose x i plus b, minus one. Set the derivative with respect to w to zero. This gives w equals the sum over i of alpha i y i x i. Set the derivative with respect to b to zero. This gives the sum of alpha i y i equals zero. Put w back into the Lagrangian. We get the dual: maximise the sum of alpha i, minus one half the double sum of alpha i alpha j y i y j, times x i transpose x j. Look at the data. They appear only as dot products, x i transpose x j.

That is the kernel trick. Replace the dot product by a kernel, k of x and z, which equals phi of x, transpose, phi of z, for some feature map phi. Example: in two dimensions, x transpose z, squared, equals the dot product of the features x one squared, the square root of two times x one x two, and x two squared. So we compute in the quadratic feature space without ever building it. The RBF kernel even corresponds to an infinite feature space. Only points with alpha larger than zero matter. These are the support vectors.

## 7 · What is the VC dimension?

Question 7. What is the VC dimension, and what is it used for?

The VC dimension is the largest number of points that a model class can shatter, that is, label in every possible way, and it measures capacity in generalization bounds.

Take linear classifiers in the plane. Three points, not on one line, can be split in all eight ways. Four points cannot. Put them on the corners of a square and label the diagonals alike, the XOR pattern. No single line separates them. So the VC dimension is three. In general, linear classifiers with a bias in d dimensions have VC dimension d plus one. What is it used for? Vapnik's bound says that, with high probability, the true risk is at most the empirical risk plus a term that grows roughly like the square root of the VC dimension times the log of N, divided by N. So a larger capacity needs more data for the same guarantee. This is the theory behind the bias-variance trade-off and the idea of structural risk minimization.

## 8 · Explain the EM algorithm

Question 8. Explain expectation maximization. When do we use it, and how does it work?

EM maximises the likelihood when some variables are hidden, by alternating an E-step that guesses the hidden variables and an M-step that refits the parameters.

When do we use it? When the likelihood would be easy if we knew a hidden variable z, for example which Gaussian component produced a point. Here is the derivation. The log-likelihood is log p of x, which is the log of the sum over z of p of x and z. Insert any distribution q of z: multiply and divide by q. Now Jensen's inequality says that the log of an average is at least the average of the log. So log p of x is at least the sum over z of q times log of p of x and z, over q. This is a lower bound. The E-step makes the bound tight. It sets q to the posterior, p of z given x and the current parameters. The M-step maximises the bound over the parameters, which means maximising the expected complete-data log-likelihood, called Q. Each round can only raise the likelihood, but it may stop in a local optimum. For a Gaussian mixture, the E-step computes the responsibility of each component for each point, and the M-step updates the means, covariances and weights with these responsibilities.

## 9 · Likelihood and the problems of maximum likelihood

Question 9. What is the likelihood, and what are the problems of maximum likelihood?

The likelihood is the probability of the observed data seen as a function of the parameters, and maximum likelihood can overfit when the data are few or the model is too flexible.

A coin shows the idea. We toss it N times and see k heads. The likelihood of the head probability theta is theta to the k, times one minus theta, to the N minus k. Take the log: k log theta plus N minus k, times log of one minus theta. Set the derivative to zero: k over theta, minus N minus k over one minus theta, equals zero. Solve it, and theta equals k over N, the observed frequency. Now the problem. Toss three times and see no heads. Then theta is zero, so the model says heads are impossible. That is overfitting to a small sample, the sunrise problem. The fix is a prior. With Laplace smoothing the estimate becomes k plus one, over N plus two. This is MAP estimation, maximum likelihood plus the log of a prior. The same prior idea, for weights, is weight decay.

## 10 · Explain attention and the transformer

Question 10. Explain attention and the transformer architecture.

Every token builds a query, a key and a value, and its output is a weighted mean of all values, with weights from the softmax of the query-key similarities.

Let us build it. Each token vector x is multiplied by three learned matrices, which gives the query q, the key k and the value v. The score between token i and token j is q i transpose k j. A softmax over j turns the scores into weights that sum to one. The output of token i is the weighted sum of all values. In matrix form, the output is softmax of Q K transpose, divided by the square root of d k, times V.

Why the square root? Suppose the components of q and k have mean zero and variance one. Their dot product is a sum of d k such products, so its variance is d k. Large scores push the softmax into saturation, where the gradients vanish. Dividing by the square root of d k brings the variance back to one. Multi-head attention runs several of these in parallel with smaller dimensions. A transformer block is attention plus a feed-forward network, each with a residual connection and layer normalization. Vaswani and colleagues, 2017.

## 11 · Is self-attention permutation invariant? What is its cost?

Question 11. Is self-attention permutation invariant? What is its cost?

Without positional encodings it is permutation equivariant, so the model cannot see order, and its cost grows with the square of the sequence length.

Let us show it. Let P be a permutation matrix that reorders the tokens. The inputs become P X, so the queries become P Q, the keys P K and the values P V. The score matrix becomes P Q times K transpose P transpose. The softmax acts row by row, so it commutes with reordering. Then we multiply by P V, and P transpose times P is the identity. What remains is P times the original output. Reorder the input, and the output is reordered in the same way. So without positions the model treats a sentence as a bag of words. That is why we add positional encodings. The cost: the score matrix has N times N entries, each a dot product of length d. So time and memory grow like N squared times d. Linear attention, state space models and the xLSTM from Linz scale linearly in N.

## 12 · The LSTM and the bidirectional RNN

Question 12. How does an LSTM solve the vanishing gradient, and how is a bidirectional RNN trained?

The LSTM keeps a cell state that is updated by addition and protected by gates, so the error can flow over many time steps, and a bidirectional RNN runs one RNN forwards and one backwards and is trained with backpropagation through time.

Why does the addition help? The cell update is c t equals f t times c t minus one, plus i t times the candidate. Take the derivative of c t with respect to c t minus one along this direct path. It is just f t, the forget gate. In the original LSTM there was no forget gate, so this factor was exactly one. Then the error passes through any number of steps without shrinking. That is the constant error carousel. A plain RNN instead multiplies by the weight matrix and the slope of tanh at every step, and that product vanishes. The input gate decides what is written, the forget gate what is kept, and the output gate what is read, h t equals o t times tanh of c t. Hochreiter and Schmidhuber, 1997.

For the bidirectional RNN, one RNN reads the sequence from left to right and another from right to left. At every position we join their two hidden states. We unroll both over the whole sequence and backpropagate through time, as for one RNN. The catch: the whole sequence must be known in advance, so it cannot run in real time.

## 13 · Derive the REINFORCE loss

Question 13. Derive the REINFORCE loss.

With the log-derivative trick, the gradient of the expected return becomes the expectation of the return times the gradient of the log-policy.

Step one. The objective is J of theta, the expected return G over trajectories tau, drawn from p theta. Write the expectation as an integral of p theta of tau times G of tau. The gradient moves inside: the integral of G times the gradient of p.

Step two, the trick. The gradient of p equals p times the gradient of log p, because the derivative of log p is the derivative of p divided by p. So the gradient of J is the integral of p times G times the gradient of log p. That is again an expectation, which we can estimate by sampling episodes.

Step three. The probability of a trajectory is the start distribution, times the product over time of the policy pi of a t given s t, times the environment transition. Take the log. The product becomes a sum. Only the policy terms depend on theta, so the environment drops out of the gradient. We get: the gradient of J equals the expectation of G times the sum over t of the gradient of log pi of a t given s t. As a loss we minimise minus G times the sum of log pi.

Step four, the baseline. Subtract a constant b from G. The extra term is b times the expectation of the gradient of log p, which is b times the gradient of the integral of p. That integral is one, so its gradient is zero. The baseline adds no bias, but it lowers the variance.

## 14 · How can you measure robustness, apart from adversarial attacks?

Question 14. How can you measure robustness, apart from adversarial attacks?

Test under noise and corruptions, test under distribution shift, check calibration and uncertainty, and bound the sensitivity with a Lipschitz constant.

The Lipschitz idea in one line. For a small change epsilon of the input, the output changes by about the gradient transposed times epsilon. Its size is at most the norm of the input gradient times the norm of epsilon. So a small input gradient means a stable model. For the whole network, the product of the spectral norms bounds this sensitivity. Beyond that, corruption benchmarks add blur, noise or weather to the test images. Out-of-distribution tests use data from another hospital, another sensor or another year. Calibration asks whether a confidence of eighty percent is really right eighty percent of the time. The expected calibration error measures the gap. Certified methods, such as randomized smoothing, even give a guaranteed radius in which the prediction cannot change.

## 15 · How do you measure accuracy, false positives, and agreement with an expert?

Question 15. How do you measure accuracy, false positives and false negatives, and the agreement with an expert? What is the AUC?

Start from the confusion matrix, then use precision, recall, F1 and the ROC AUC, and use Cohen's kappa for the agreement with an expert.

The confusion matrix counts true positives, false positives, false negatives and true negatives. Precision is TP over TP plus FP: of all predicted positives, how many are right. Recall is TP over TP plus FN: of all real positives, how many we find. F1 is their harmonic mean, two P R over P plus R, which stays low if either one is low. Why not plain accuracy? With nine hundred inactive and one hundred active molecules, a model that always says inactive has ninety percent accuracy and finds nothing.

The ROC curve plots the true positive rate against the false positive rate over all thresholds. The AUC has a clear meaning: it is the probability that a random positive gets a higher score than a random negative. So an AUC of 0.97 means that in ninety-seven of a hundred such pairs the positive is ranked higher. One half is random guessing.

For the expert, Cohen's kappa corrects the observed agreement for chance. Kappa equals p o minus p e, over one minus p e. Here p o is the observed agreement, and p e is the agreement we would expect by chance, from the two raters' marginal frequencies. Kappa is one for perfect agreement and zero for chance level.

# Q1 · Questions and answers: Machine Learning, October 2026

These are the machine learning questions from the defenses in October 2026, with Professor Hochreiter and Professor Schlüter. After each question there is a short pause. Say your answer aloud first. Then listen to the model answer. The first sentence is the part to learn by heart. After it, we build the formula step by step, so you can derive it on the board instead of reciting it.

## 1 · How is the value of a single neuron computed?

Question 1. How is the value of a single neuron computed?

A neuron takes a weighted sum of its inputs, adds a bias, and passes the result through a non-linear activation function.

Let us build it. The neuron receives inputs a one to a n from the layer below. Each input gets its own weight, w j. We multiply and add, and we add a bias b. This number is the pre-activation, s, the sum over j of w j times a j, plus b. Then we apply the activation function, so the output is a equals f of s. Two steps to remember: first sum, then bend.

## 2 · What is deep learning, and what happens in a layer?

Question 2. What is deep learning? What is a layer, and what happens in a layer?

Deep learning trains a network of many layers end to end, and every layer turns the representation of the layer below into a more useful one.

Now go from one neuron to a layer. A layer is many neurons that read the same input. Each neuron has its own row of weights. If we stack these rows, we get a weight matrix W, and the biases form a vector b. So the whole layer computes s equals W times a, plus b, and then a new equals f of s, element by element. The network repeats this, layer after layer. Early layers find simple features, such as edges. Later layers combine them into parts and objects. We never design these features by hand. The network learns them from data. So a layer is a linear map, then a bend. And deep means features built from features.

## 3 · What happens without activation functions?

Question 3. What is the difference between a deep network with and without activation functions?

Without activation functions the whole network collapses into one linear map, so depth adds nothing.

We can show it in two lines. Take two layers without f. The first gives W one x plus b one. The second gives W two times that, plus b two. Multiply it out: W two W one x, plus W two b one plus b two. Now call W two W one a new matrix, W prime, and call the rest a new bias, b prime. So the result is W prime x plus b prime, which is again one linear layer. This holds for any number of layers. A linear model cannot even solve XOR. The non-linearity is what makes depth useful.

## 4 · Can an activation function be linear?

Question 4. Can an activation function be linear?

At the output, yes, for regression. In the hidden layers, no, because linear times linear stays linear.

The last answer is the reason for the hidden layers. For the output, think about the target. In regression the target can be any real number, so we should not squeeze it into a range. A linear output, the identity, is the right choice. With squared loss it also gives a clean delta, prediction minus target. So the rule is simple. Linear at the output for regression. Non-linear in every hidden layer.

## 5 · Supervised or unsupervised?

Question 5. Supervised or unsupervised learning: what is the difference, and why choose one?

Supervised learning has a label for every input and learns the map from input to label, while unsupervised learning has no labels and looks for structure in the inputs.

In supervised learning the data are pairs, x and y, and the model learns to predict y from x. Classification and regression are supervised. In unsupervised learning we only have x. We look for clusters, for the density of the data, or for a few main directions, as in PCA. Self-supervised learning sits in between. It creates its own labels from the data, for example by predicting the next word. How to choose? If I have a clear target and labelled data, I choose supervised. If I have no labels, or I want to explore the data first, I choose unsupervised.

## 6 · Write down empirical risk minimization

Question 6. Write down empirical risk minimization.

We cannot compute the true risk, so we replace the expected loss by its average over the training data and minimise that average.

Let us derive it. We have N data pairs, x n and y n, drawn independently from an unknown distribution p of x and y. The model g maps x to a prediction, y hat, and has parameters w. The loss L of y and y hat says how wrong one prediction is. What we really want is a small true risk. That is the expected loss, R of g, equals the expectation over p of L of y and g of x. But p is unknown, so we cannot compute this expectation. The law of large numbers helps us. A sample mean approaches the expectation. So we replace the expectation by the mean over our data. This gives the empirical risk, R hat, equals one over N, times the sum over n of L of y n and g of x n. Training means minimising R hat over w.

A simple example is linear regression. The model is w transpose x, and the loss is the squared error. So R hat is one over N times the sum of y n minus w transpose x n, squared. Set the gradient to zero. This gives X transpose X times w equals X transpose y. So w equals the inverse of X transpose X, times X transpose y. These are the normal equations, the least-squares solution.

## 7 · Empirical error versus generalization error

Question 7. What is the difference between the empirical error and the generalization error?

The empirical error is the average loss on the training data, while the generalization error is the expected loss on new data from the same distribution.

The two differ for one reason. We chose the weights by looking at the training data. So the training error is an optimistic estimate. It is biased downwards. The generalization error is the true risk from the last answer, and we estimate it on data the model has never seen, a test set or cross-validation. The difference between the two is the generalization gap. A large gap means overfitting. Theory says the gap grows with the capacity of the model, for example its VC dimension, and shrinks as the number of samples N grows. So more data or a simpler model reduces the gap.

## 8 · Explain gradient descent and the weight update

Question 8. Explain gradient descent and the weight update.

Gradient descent moves the weights a small step against the gradient, w becomes w minus eta times the gradient of the empirical risk.

Why the minus sign? Use a first-order Taylor expansion. If we change the weights by a small delta w, the risk changes by about the gradient, transposed, times delta w. Now choose delta w as minus eta times the gradient. Then the change of the risk is minus eta times the squared norm of the gradient. A squared norm is never negative. So for a small enough eta the risk goes down. This is the whole idea. The gradient points uphill, so we step the other way. Eta, the learning rate, sets the size of the step.

## 9 · Why do we use mini-batches?

Question 9. Why do we use mini-batches?

A mini-batch gives an unbiased and cheap estimate of the full gradient, it runs in parallel on a GPU, and its small noise helps generalization.

Here is the reason in symbols. The empirical risk is a mean over N samples. So its gradient is also a mean, the average of the per-sample gradients. Now pick B samples at random and average only their gradients. The expected value of this average is the full gradient, so the estimate is unbiased. Its variance is the per-sample variance divided by B. So the standard deviation falls like one over the square root of B, while the cost grows like B. Doubling the batch costs twice as much but removes only about thirty percent of the noise. That is why a moderate batch is the best trade-off. The remaining noise is even useful, because it helps to leave sharp minima.

## 10 · Derive backpropagation and the delta errors

Question 10. Derive backpropagation and the recursive formula for the delta errors.

The delta of a unit is the derivative of the loss with respect to its pre-activation, the weight gradient is the delta above times the activation below, and the deltas are computed backwards with the chain rule.

Step one, the definition. Delta i equals the partial derivative of L with respect to s i.

Step two, the weight gradient. The weight w i j acts on the loss only through s i. So by the chain rule, the derivative of L with respect to w i j is delta i times the derivative of s i with respect to w i j. And s i is the weighted sum, the sum over j of w i j times a j. Its derivative with respect to w i j is simply a j. So the gradient is delta i times a j.

Step three, the recursion. A hidden unit j influences the loss only through the units k of the next layer. So we sum over all these paths. The derivative of L with respect to s j is the sum over k of three factors. First, the derivative of L with respect to s k, which is delta k. Second, the derivative of s k with respect to a j, which is the weight w k j. Third, the derivative of a j with respect to s j, which is f prime of s j. So delta j equals f prime of s j, times the sum over k of w k j times delta k.

Step four, the start. At the output, for squared loss one half of a minus y, squared, the delta is a minus y, times f prime of s. Then we go backwards, layer by layer. In matrix form: multiply the deltas above by W transposed, then element by element by f prime. One forward pass and one backward pass give every gradient, at a cost linear in the number of weights.

## 11 · The output delta for softmax with cross-entropy

Question 11. What is the output delta for softmax with cross-entropy?

It is simply the prediction minus the label, a i minus y i.

Let us derive it. The softmax output is a k equals e to the s k, divided by the sum over all classes of e to the s. The cross-entropy loss with a one-hot label is L equals minus the sum over k of y k times log a k. First we need the derivative of the softmax. Using the quotient rule, the derivative of a k with respect to s i is a k times, one if k equals i, minus a i. Now apply the chain rule. The derivative of L with respect to s i is minus the sum over k of y k over a k, times that softmax derivative. The a k cancels. We get minus y i, plus a i times the sum over k of y k. A one-hot label sums to one. So the delta is a i minus y i. The same clean result holds for a sigmoid with binary cross-entropy, and for a linear output with squared loss.

## 12 · Binary classification: why a sigmoid, and why not a step?

Question 12. Binary classification with labels 0 and 1: what is the output, why a sigmoid, and could we use a step function instead?

The output is the probability of class one, the sigmoid gives a smooth value between zero and one, and a step function cannot be trained with backpropagation because its derivative is zero almost everywhere.

First the sigmoid. It is sigma of s equals one over one plus e to the minus s. Its derivative is e to the minus s, over one plus e to the minus s, squared. We can write this as sigma times, one minus sigma. So the slope is largest at s equals zero, where it is one half times one half, a quarter.

Now the loss. Binary cross-entropy is L equals minus, y log a, plus one minus y, times log of one minus a. Its derivative with respect to a is a minus y, divided by a times one minus a. Multiply by the sigmoid slope, a times one minus a. These factors cancel, and the delta is a minus y. Clean and never stuck.

Now the step function. For the final decision it would give the same answer as a threshold at one half. But its derivative is zero everywhere except at zero, where it is not defined. So every delta is zero, and no weight ever changes. The old perceptron used a step, but with its own update rule, not with backpropagation. A flat step means zero gradient, and zero gradient means no learning.

## 13 · Which activation functions do you know, and which one is from Linz?

Question 13. Which activation functions do you know, and which one is from Linz?

Sigmoid, tanh, ReLU, leaky ReLU and GELU, and from Linz the ELU and the SELU, which makes a network self-normalizing.

Sigmoid and tanh are smooth, but they saturate. We just derived that the sigmoid slope is at most a quarter, so deep networks with sigmoids lose their gradient. ReLU, the maximum of zero and s, has slope one for positive inputs, so it does not saturate there. But a unit whose input stays negative never learns again, a dead unit. ELU, from Clevert, Unterthiner and Hochreiter, replaces the negative part by alpha times, e to the s, minus one. It is smooth and pushes the mean activation towards zero. SELU, from Klambauer and colleagues in 2017, multiplies ELU by a constant lambda. With lambda about 1.0507 and alpha about 1.6733, the mean and variance of the activations are pulled to zero and one, layer after layer, without batch normalization.

## 14 · The learning rate: why small, why large?

Question 14. How does the learning rate influence training? Why small, why large?

The learning rate is the step size, too small and training is slow, too large and the loss oscillates or diverges.

We can see the limit with a simple model. Near a minimum, the loss along one direction looks like a parabola, one half times h times w squared, where h is the curvature. The gradient is h times w. So one step gives w new equals w minus eta h w, which is one minus eta h, times w. Every step multiplies the distance to the minimum by the factor one minus eta h. If this factor is between minus one and one, we converge. That means eta must be smaller than two over h. If eta is tiny, the factor is close to one, so we crawl. If eta is above two over h, the factor is larger than one in size, and we jump further away each time. That is divergence. In practice we use a moderate rate, a short warm-up, and then a decay, for example a cosine schedule.

## 15 · Learning rate versus batch size

Question 15. Learning rate versus batch size: how are they related?

A larger batch gives a less noisy gradient, so it can take a larger step, and a common rule scales the learning rate linearly with the batch size.

Here is the argument of the linear scaling rule, from Goyal and colleagues in 2017. Take k small steps, each with batch size B and learning rate eta. If the gradient changes little over these steps, the total move is about eta times the sum of k gradient estimates. Now take one big step with batch size k times B. Its gradient is the average of the same k times B samples. To move the same distance, this step needs the rate k times eta. So multiply the batch by k, and multiply the rate by k. The noise also tells the story: the noise of the step grows with eta and shrinks with B, so the ratio eta over B sets the noise level. The rule breaks down at the very start, which is why we warm up, and for very large batches, where the gradient is already almost exact.

## 16 · Gradient descent versus Adam on mini-batches

Question 16. Gradient descent versus Adam on mini-batches: how does each one use the data?

Both take one step per mini-batch, but SGD uses only the current gradient with one global learning rate, while Adam keeps running averages of past gradients and gives every weight its own step size.

First the data. We shuffle the training set, cut it into mini-batches, and take one step per batch. One pass over all batches is one epoch. Both optimizers do this.

Now Adam. Let g be the gradient of the current batch. Adam keeps a first moment, m equals beta one times m, plus one minus beta one, times g. This is momentum, an average over past batches. It also keeps a second moment, v, the same average but of g squared. Both start at zero, so in the first steps they are too small. If we unroll m, its expected value is the true mean times one minus beta one to the power t. So we divide by that factor. This is the bias correction, m hat and v hat. The step is eta times m hat, divided by the square root of v hat plus epsilon.

Why does this help? Suppose all gradients of one weight are multiplied by a constant c. Then m hat grows by c and the square root of v hat also grows by c. The step stays the same. So Adam does not care about the scale of each gradient, and every weight gets a sensible step. Plain SGD forgets the past batches. Adam remembers.

## 17 · Which optimizers do you know? AdamW versus Adam with L2

Question 17. Which optimizers do you know? What is the difference between AdamW and Adam with L2?

SGD, momentum, Nesterov, AdaGrad, RMSprop, Adam and AdamW, and AdamW applies the weight decay directly to the weights instead of passing it through the adaptive division.

Let us compare the two. With L2 we add lambda over two times the squared norm of w to the loss. Its gradient is lambda times w. For plain SGD the update becomes w minus eta, times g plus lambda w. We can write this as one minus eta lambda, times w, minus eta g. So the weights shrink by a constant factor every step. For SGD, L2 and weight decay are the same.

For Adam they are not. The term lambda w goes into the moments and is then divided by the square root of v hat. A weight with large gradients has a large v hat, so its decay becomes small. The regularization is weakest exactly where the weights move most. AdamW, from Loshchilov and Hutter, decouples the two. The update is w minus eta, times m hat over the square root of v hat, plus lambda w. Now the decay is outside the division, and every weight decays at the same rate. Remember: AdamW keeps the decay outside the division.

## 18 · What are vanishing and exploding gradients?

Question 18. What are vanishing and exploding gradients?

The delta of an early layer is a product of one factor per layer, so it shrinks to zero or grows without bound when these factors are below or above one.

Go back to the recursion. The delta of a layer is f prime times W transposed times the delta of the layer above. Apply it again and again. The delta of the first layer is a product over all layers of f prime and W transposed. Now take norms. The size of this product is at most the product of the spectral norms of the W, times the largest slope of f, for every layer. With the sigmoid, the largest slope is a quarter. So if a quarter times the norm of W is below one, the delta shrinks like that number to the power of the depth. That is exponential decay. If the factor is above one, it grows exponentially. Sepp Hochreiter analysed this problem in his diploma thesis in 1991, here in Linz.

## 19 · How can we mitigate vanishing gradients, and which structure do we want for W?

Question 19. How can we mitigate vanishing gradients, and which structure do we want for W during learning?

We keep every factor of the backward product close to one, and ideally W stays close to an isometry, with singular values near one.

From the last answer, every fix has the same goal. A careful initialization sets the scale right at the start. Activations like ReLU, ELU or SELU have a slope of one, or close to it, instead of a quarter. Normalization layers keep the activations at a fixed scale. Residual connections change the layer to a new equals a plus F of a. Then the Jacobian is the identity plus the Jacobian of F. A product of terms like one plus something small does not vanish. For sequences, the LSTM keeps a memory cell with a constant error flow. And gradient clipping limits explosion.

Which structure for W? If all singular values of W are one, W is orthogonal. It rotates the vector but does not stretch it, so signals and deltas keep their size. That is the idea of orthogonal initialization. During training the weights learn structure and their norms tend to grow. We want the spectral norm to stay bounded, for example through weight decay or spectral normalization.

## 20 · How should the weights be initialized, and why this variance?

Question 20. Which initialization techniques do you know, and why do we use this variance?

LeCun, Glorot and He initialization choose the weight variance so that the variance of the signal stays the same from layer to layer.

Let us derive it. A pre-activation is s equals the sum over n in terms of w j times a j. Assume the weights are independent of the inputs and have zero mean. Then the variance of a sum of independent terms is the sum of the variances. Each term has variance equal to the variance of w times the mean square of a. So the variance of s is n in, times the variance of w, times the mean square of a. We want this to stay constant through the layers. So we choose the variance of w as one over n in. That is LeCun initialization, the one used with SELU.

For ReLU, half of the inputs become zero, so the mean square of a is only half the variance of s. To compensate, we double the weights' variance: two over n in. That is He initialization.

The backward pass has the same problem, but the deltas are summed over n out units. There we would need one over n out. Glorot, also called Xavier, takes the compromise: two over the sum of n in and n out. And why not all zeros? Then all units in a layer compute the same thing and get the same update, so they never become different. Random weights break this symmetry.

## 21 · The spectral norm, and why it matters

Question 21. What is the spectral norm of a weight matrix, and why does it matter?

The spectral norm is the largest singular value of W, the largest factor by which the layer can stretch a vector.

The definition is the maximum, over all non-zero x, of the norm of W x divided by the norm of x. If we square this, we get x transpose W transpose W x over x transpose x. That ratio is largest for the top eigenvector of W transpose W. So the spectral norm is the square root of the largest eigenvalue of W transpose W, which is the largest singular value.

Why does it matter? Take two inputs, x and x prime. One layer stretches their difference by at most the spectral norm of W. Activations like ReLU or tanh have slope at most one, so they do not stretch it further. Chain the layers together. The output difference is at most the product of all spectral norms, times the input difference. So this product bounds the Lipschitz constant of the network. A large product means exploding signals and a network that is sensitive to small changes in the input. Spectral normalization divides W by its spectral norm, which is used for robustness and in GANs.

## 22 · Batch norm, layer norm and RMSNorm

Question 22. Which normalizations do you know, and which one is popular now?

Batch norm normalizes each feature over the mini-batch, layer norm normalizes over the features of one sample, and RMSNorm, the popular one now, only divides by the root mean square without subtracting the mean.

Let us write them as one recipe. Take a set of numbers. Subtract their mean, mu. Divide by their standard deviation, the square root of the variance plus a small epsilon. Then rescale with a learned gain, gamma, and shift with a learned beta. The only question is which set of numbers we use. Batch norm uses one feature across all samples in the batch. So it depends on the batch, it needs running statistics at test time, and it struggles with small batches. Layer norm uses all features of one sample. It works the same at training and test time, so it suits transformers and recurrent networks. RMSNorm, from Zhang and Sennrich, drops the mean. It divides x by the square root of one over d times the sum of x squared, plus epsilon, and multiplies by a gain. The idea is that the rescaling, not the re-centring, is what stabilizes training. It is cheaper and works as well, so large language models such as LLaMA use it.

## 23 · Which regularization techniques do you know?

Question 23. Which regularization techniques do you know?

Weight decay, dropout, early stopping, data augmentation and noise, and all of them reduce the gap between training and test error.

Let us derive the name weight decay. We add lambda over two times the squared norm of w to the empirical risk. Its gradient adds lambda times w. So the update is w minus eta, times the risk gradient plus lambda w. Rearranged, that is one minus eta lambda, times w, minus eta times the risk gradient. Before every normal step, the weights shrink by the factor one minus eta lambda. They decay. L1 instead adds the sum of absolute values and pushes weights to exactly zero, so it makes the model sparse.

Dropout switches each unit off with some probability during training. We keep a unit with probability p and divide its output by p. Then the expected output stays the same, so nothing changes at test time. The network cannot rely on any single unit. Early stopping ends training when the validation error starts to rise. Data augmentation adds transformed copies of the inputs, such as flips or crops.

## 24 · The SVM primal, and the famous one

Question 24. Write down the SVM primal. What do we optimize, where does the 1 in the constraints come from, and could we use another value?

We maximise the margin, and the one only fixes the scale of w and b, so any positive value would give the same hyperplane.

Start from geometry. The distance of a point x i to the hyperplane w transpose x plus b equals zero is the absolute value of w transpose x i plus b, divided by the norm of w. Now notice a free scale. If we multiply w and b by any positive constant, the hyperplane stays the same. So we may fix the scale. We choose it so that the closest points give y i times, w transpose x i plus b, equal to exactly one. This is the canonical form, the canonical hyperplane. Then the closest points have distance one over the norm of w, on each side. The margin is two over the norm of w.

Maximising two over the norm of w is the same as minimising the norm. We minimise one half of the squared norm instead, because it is smooth and convex, and the one half makes the derivative clean. So the primal is: minimise one half the squared norm of w, subject to y i times, w transpose x i plus b, at least one, for every i. With slack variables xi i and a penalty C, we get the soft margin.

Could we use c instead of one? Yes. Put w prime equals w over c, and b prime equals b over c. The constraint with c becomes the constraint with one for w prime. The solution is just rescaled, the same hyperplane and the same classifier. One is simply the natural choice.

## 25 · The receptive field of a CNN

Question 25. What is the receptive field of a CNN, how can we increase it, and what does pooling do?

The receptive field is the part of the input that can influence one unit, and it grows with depth, kernel size, stride or pooling, and dilation.

Let us derive how it grows. Start with one input pixel, a receptive field of one. A convolution with kernel size k looks at k neighbours, so it adds k minus one to the field. But in a deeper layer, neighbours are not one input pixel apart. They are as far apart as the product of all earlier strides. Call this the jump, j. So the rule is: r new equals r old, plus k minus one, times j. Example: three layers of three by three, stride one. Each adds two, so the field is one plus two plus two plus two, which is seven. If a pooling layer with stride two comes first, the jump doubles, and every later layer adds twice as much. A dilated convolution with dilation d spreads the kernel, so it covers d times k minus one, plus one, input positions, with the same number of weights.

Pooling takes the maximum or the average in a small window. It has no weights, it shrinks the map, it enlarges the receptive field of the following layers, and it adds a little invariance to small shifts. Global average pooling gives one vector for the whole image or the whole sequence.

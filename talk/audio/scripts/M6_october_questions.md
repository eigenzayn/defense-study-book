# M6 · The October questions: layers, outputs, step sizes and stable training

This episode collects the machine learning questions from the defenses in October 2026. Professor Schlüter asked about layers, the sigmoid, the learning rate and the receptive field. Professor Hochreiter went deeper: initialization, the spectral norm, normalization, AdamW and the SVM. For every question, learn the first sentence by heart. Then add one detail.

## What is deep learning, and what is a layer?

Deep learning means training a network with many layers, end to end, from data. Each layer turns the representation from the layer below into a more useful one.

What happens inside a layer? Two things. First a linear map: the weights times the input, plus a bias. Then a non-linear function on every unit. Early layers find simple features, like edges. Later layers combine them into parts and objects. Nobody designs these features. The network learns them. So remember: a layer is linear, then bend. Deep means features built from features.

## Supervised or unsupervised?

Supervised learning has a label for every input, and it learns the map from input to label. Classification and regression are supervised. Unsupervised learning has no labels. It looks for structure, for example clusters, a density, or a few main directions with PCA. Self-supervised learning makes its own labels from the data, like predicting the next word.

Why choose supervised? Because I have a clear target and labelled data. With no labels, or when I first want to explore the data, I choose unsupervised.

## Binary classification: why a sigmoid, and why not a step?

With labels zero and one, the network gives one number: the probability of class one. The sigmoid squeezes any real number into the range from zero to one, so it fits. At test time we threshold it, usually at one half.

Could a step function do the same job? For the final decision, yes. For learning, no. The step is flat everywhere except at zero, where it jumps. So its derivative is zero almost everywhere, and at zero it is not defined. Then every delta is zero, and no weight ever changes. The old perceptron did use a step, but with its own learning rule, not backpropagation.

One more point. The sigmoid together with binary cross-entropy gives the clean output delta: prediction minus label. Short version: a flat step means zero gradient, and zero gradient means no learning.

## Can an activation function be linear?

At the output, yes. For regression the target can be any real number, so the output is linear. In the hidden layers, no. Two linear maps in a row are just one linear map. W two times W one is one matrix. So a deep linear network is only a linear model, and it cannot solve XOR. Linear times linear stays linear.

## The learning rate

The learning rate is the size of each step down the loss. Picture a walk into a valley in fog. Tiny steps are safe, but you need forever, and you may stop in a small dip. Huge steps jump over the valley, and you land higher on the other side. Then the loss oscillates or even diverges.

In practice we start with a moderate rate, often after a short warm-up, and then let it decay, for example with a cosine schedule. A larger rate also adds noise, and that noise can help to find flat minima, which tend to generalize better.

## Learning rate and batch size

A bigger batch gives a less noisy gradient, so we can afford a bigger step. The noise of stochastic gradient descent depends roughly on the learning rate divided by the batch size. A common rule is linear scaling, used by Goyal and colleagues in 2017: double the batch, double the rate, and warm up at the start. But very large batches stop paying off, because the gradient is already almost exact. Remember: batch times two, step times two.

## Gradient descent versus Adam, batch by batch

First, how the data are used. We shuffle the training set, cut it into mini-batches, and take one step per mini-batch. One pass over all batches is one epoch. Both optimizers work like this.

The difference is memory. Plain SGD forgets. Each step uses only the gradient of the current batch, with one learning rate for all weights. Adam remembers. It keeps a running average of the gradients, which is momentum and smooths the noise from batch to batch. It also keeps a running average of the squared gradients, and divides by its square root. So every weight gets its own step size. Weights with large gradients take smaller steps, and rare weights take larger ones. A bias correction fixes the first few steps, when the averages still start from zero.

Adam is fast and needs little tuning, so it is the usual default. SGD with momentum sometimes generalizes a little better. Short version: SGD forgets, Adam remembers.

## AdamW versus Adam with weight decay

This was Professor Hochreiter's question. If we add an L2 penalty to the loss, its gradient, lambda times w, goes into Adam together with the normal gradient. Then Adam divides it by the square root of the second moment. So weights with large gradients get almost no decay. The regularization is weaker exactly where we want it.

AdamW, from Loshchilov and Hutter, decouples the two. The Adam step uses only the loss gradient, and the decay is applied directly to the weights, outside the division. For plain SGD, L2 and weight decay are the same thing. For Adam they are not. Remember: AdamW keeps the decay outside the division.

## Which normalizations do you know?

Batch normalization normalizes each feature over the mini-batch. It depends on the batch, so it needs running statistics at test time and struggles with small batches. Layer normalization normalizes over the features of one sample, so it suits transformers and recurrent networks. RMSNorm, from Zhang and Sennrich, is now the popular one in large language models. It only divides by the root mean square of the features, with a learned gain. It does not subtract the mean, so it is cheaper, and it works just as well. Remember: batch norm goes across samples, layer norm across features, RMSNorm without the mean.

## Initialization, and the theory behind the variance

Which initializations do you know? LeCun, Glorot, also called Xavier, He, and orthogonal initialization. Biases usually start at zero.

Why this variance? A pre-activation is a sum over n in terms, weight times input. Its variance is n in times the weight variance times the input variance. We want this to stay the same from layer to layer. So the weight variance is one over n in. That is LeCun, and it is the one used with SELU. ReLU sets half of the units to zero, so He doubles it: two over n in. The backward pass has the same problem, but with n out. Glorot takes the compromise: two over the sum of n in and n out. The theory is simple: keep the variance of the signals going forward, and of the deltas going backward, constant.

## The spectral norm, and the structure we want for W

The spectral norm of W is its largest singular value. It is the largest factor by which the layer can stretch a vector. The product of the spectral norms over all layers bounds how much the whole network can stretch its input, so it bounds exploding signals and the sensitivity to small changes.

Which structure do we want? Ideally W is close to an isometry, with all singular values near one, like an orthogonal matrix. Then signals and deltas keep their size through many layers, which is the point of orthogonal initialization. During training the weights move away from random and learn structure, and their norms tend to grow. We want the spectral norm to stay bounded, for example with weight decay or with spectral normalization, which divides W by its largest singular value.

## How to fight vanishing gradients

The delta of the first layer is a product of one Jacobian per layer. Factors below one make it vanish. Factors above one make it explode. So every fix keeps the factors close to one. Good initialization. Non-saturating activations, like ReLU, ELU or SELU. Normalization layers. Residual connections, so that each Jacobian is close to the identity. Gradient clipping against explosion. And for sequences, the LSTM. Remember: keep the factors near one.

## The SVM primal, and the famous one

Write it down: minimise one half the squared norm of w, subject to y i times, w transpose x i plus b, being at least one, for every point. What do we optimize? The margin. The margin is two over the norm of w, so a small norm means a wide margin.

Where does the one come from? From a free scale. The hyperplane with w and b is the same as the hyperplane with two w and two b. So we fix the scale by asking that the closest points give exactly plus or minus one. That is the canonical form, or the canonical hyperplane.

Could we use another value? Yes, any positive number c. The solution is then just c times w, and c times b. The same hyperplane, the same classifier. One is simply the natural choice. Short version: the one only fixes the scale.

## The receptive field

The receptive field of a unit is the part of the input that can influence it. With three by three kernels and stride one, each layer adds only two pixels, so the field grows slowly.

How to increase it? More layers. Larger kernels. Strides or pooling, which multiply the growth, because later layers work on a coarser grid. And dilated convolutions, which skip pixels and grow the field fast without losing resolution.

Pooling takes the maximum or the average in a small window. It has no weights, it shrinks the map, and it adds a little invariance to small shifts. Global average pooling gives one vector for the whole image, or the whole sequence.

## Three things to remember

One. A step function has zero gradient, so it cannot be trained with backprop. The sigmoid gives a probability, and with cross-entropy the output delta is prediction minus label.

Two. Step size and stability. The learning rate scales with the batch size. Adam remembers past gradients, and AdamW keeps the decay outside the division. Keep the variance and the singular values near one.

Three. The SVM constraint uses one only to fix the scale of w. And the receptive field grows with depth, kernel size, stride, pooling and dilation.

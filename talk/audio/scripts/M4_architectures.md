# M4 · Architectures: CNN, ResNet, RNN, LSTM and the Transformer

In most exams, after the core, the examiner picks one architecture and asks you to explain it. So for each architecture, have three things ready: the idea in one sentence, why it works, and the one formula that shows it.

## Convolutional networks

The idea: small filters with shared weights slide over the image, so a pattern is found wherever it appears.

Why does this work for images? Images have local structure: neighbouring pixels belong together. And the same pattern, an edge or an eye, can appear anywhere. Shared weights give you very few parameters and translation equivariance: shift the image, and the feature map shifts with it. Pooling makes the map smaller and adds a little invariance. And deeper layers see larger parts of the image.

The number to know: the output size is the floor of n plus two p minus k, divided by s, plus one. Here n is the input size, k the kernel, p the padding, and s the stride.

## ResNet and U-Net

ResNet adds the input of a block to its output. The next activation equals the current activation plus F of the current activation. Why does that help? The Jacobian of a residual block is the identity plus a small part. So it does not shrink the delta. Gradients can travel through very deep networks. It is like an express lift next to the stairs.

U-Net is for segmentation. It is an encoder and a decoder with skip connections between them. It predicts one class per pixel, and the skips copy fine detail from the encoder to the decoder. Professor Klambauer has asked about U-Net before.

## Recurrent networks

The idea: an RNN reads a sequence step by step and keeps a hidden state that carries the past.

The forward pass: s of t equals W times x of t, plus R times a of t minus one. Then a of t is f of s of t. The same weights are used at every step, so the number of parameters does not grow with the length of the sequence.

How is it trained? With backpropagation through time. Unfold the network over the sequence, and backpropagate as in a deep network with shared weights. The delta at each step gets two contributions: one from the output at that step, and one from the next step. And because the weights are shared, their gradient is a sum over time.

## Why plain RNNs fail, and how LSTM fixes it

At every step back in time, the delta is multiplied by the recurrent Jacobian. Over a long sequence, that product vanishes. So a plain RNN forgets long-range dependencies. This is the same vanishing gradient problem, now in time.

The LSTM, from Hochreiter and Schmidhuber in 1997, fixes it with a memory cell that is updated by addition. The cell c of t equals the forget gate times the old cell, plus the input gate times the new input. The output gate decides what to read from the cell.

The key line: the derivative of c of t with respect to c of t minus one is just the forget gate. When the forget gate is near one, that derivative is near the identity. So the error flows back through time without shrinking. This is the constant error carousel. Picture a conveyor belt that carries the memory forward, and the gates are workers who decide what goes on the belt, what stays, and what is taken off.

## Bidirectional RNNs and sequence labels

Professor Schlüter once asked about an "RNN from the future". A bidirectional RNN runs one RNN forward and one backward, and joins their states. So every step sees both the past and the future. The limit: it needs the whole sequence, so it is not for real-time use.

For one label per sequence, use the last hidden state, or pool all hidden states, and put a classifier on top.

## Attention and the Transformer

The idea: every token takes a weighted mean of all tokens, and the weights come from query times key.

Each token makes three vectors by linear maps: a query, a key and a value. The attention weights are the softmax of query times key, divided by the square root of d k. The output mixes the values with those weights.

Why divide by the square root of d k? If the entries of query and key are independent with variance one, their dot product has variance d k. Dividing by its square root brings the variance back to one, so the softmax does not saturate.

A Transformer block is multi-head self-attention plus an MLP, each with a residual connection and layer normalization.

## Two follow-up questions

Professor Lehner has asked: Transformers are permutation-equivariant, why is that a problem? Because self-attention sees the tokens as a set. Shuffle the tokens, and the outputs shuffle the same way. The order of words is lost. So we add position information: fixed sinusoids, learned vectors, or relative encodings such as RoPE.

And: compare the cost of an RNN and a Transformer. An RNN is linear in the sequence length, order N, but it is sequential. A Transformer is quadratic, order N squared, because every token attends to every token, but all tokens are processed in parallel, and long-range paths are only one step long. That is also why LSTM-style models like xLSTM are attractive again: their inference is linear in N.

## Three things to remember

One. CNN: local filters, shared weights, pooling. ResNet: identity plus residual, so the Jacobian stays near the identity.

Two. RNN: same weights every step, trained by backpropagation through time. LSTM: additive cell update, so with the forget gate near one, the error is carried unchanged.

Three. Attention: softmax of query times key over the square root of d k, times the values. Transformers need position information, and cost N squared but run in parallel.

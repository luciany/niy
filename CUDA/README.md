[Niy](https://github.com/microic/niy)
====

While other deep learning frameworks can support GPU by simply using cuDNN, cuDNN is not suitable for Niy due to the following reasons:
* Niy removes activation functions(sigmoid, tanh, relu, prelu...)
* Niy uses deconvolution(the reverse operation of convolution), not transposed convolution
* Niy tries to remove all the matrix operations so as to be closer to biological neural network


To support parallel computing, one good choice is CUDA, and we will go deep into CUDA programming


Because moving data between GPU and CPU is expensive, the whole training process should be accomplished by only GPU, without the participation of CPU





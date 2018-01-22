[Niy](https://github.com/microic/niy)
====

While other deep learning frameworks can support GPU by simply using cuDNN, cuDNN is not suitable for Niy due to the following reasons:
* Niy removes activation functions(sigmoid, tanh, relu, prelu...)
* Niy uses deconvolution(the reverse operation of convolution), not transposed convolution
* Niy tries to remove all the matrix operations so as to be closer to biological neural network


To support parallel computing, one good choice is CUDA, and we will go deep into CUDA programming


Because swithing between GPU and CPU is expensive, the whole training process should be accomplished by only GPU, without the participation of CPU


When using CUDA8, we use the following code for the whole training process:
>
	for (int i = 0; i <　number_of_samples; i++) {
		for (int j = 0; j < number_of_layers; j++) {
			// Kernel invocation
			forward_and_backward<<<dimGrid, dimBlock>>>(i, j);
		}
	}

As you can see, each sample, each layer, the kernel is stopped once just for the sake of synchronizing


CUDA9 introduces some new functions, so we can rewrite the above code:
>
	// Kernel invocation
	forward_and_backward<<<dimGrid, dimBlock>>>();

At this time, we just need to start the kernel once for the whole training process



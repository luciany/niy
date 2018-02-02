[Niy](https://github.com/microic/niy)
====
While other deep learning frameworks can support GPU by simply using cuDNN, cuDNN is not suitable for Niy

To support parallel computing, one good choice is CUDA, and we will go deep into CUDA programming


Because swithing between GPU and CPU is expensive, the whole training process should be accomplished by only GPU(without the participation of CPU)


When using CUDA8, we use the following code for the whole training process:
>
	for (int i = 0; i <　number_of_samples; i++) {
		for (int j = 0; j <= number_of_layers - 1; j++) {
			// kernel invocation
			forward<<<dimGrid, dimBlock>>>(i, j);
		}
		for (int j = number_of_layers - 1; j >= 0; j--) {
			// kernel invocation
			backward<<<dimGrid, dimBlock>>>(i, j);
			update<<<dimGrid, dimBlock>>>(j);
		}
	}

As you can see, each sample, each layer, the kernel is stopped multi times just for the sake of synchronizing


CUDA9 introduces some new functions, so we can rewrite the above code:
>
	// kernel invocation
	forward_backward_update<<<dimGrid, dimBlock>>>();

At this time, we just need to start the kernel once for the whole training process


We still need to do a lot of tests to see if our idea is practical
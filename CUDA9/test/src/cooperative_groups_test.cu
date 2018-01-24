using namespace cooperative_groups;

__global__ 
void cooperative_kernel(int *dev_buf) {

	// it seems that CUDA9 do not support sm_21

	printf("cooperative_kernel\n");

	thread_group block = this_thread_block();
	thread_group tile32 = tiled_partition(block, 32);

	if (block.thread_rank() < 32) {
	    tile32.sync();
	}

	block.sync();

	dev_buf[0] = 2;
}

void test() {
   	#define BUF_SIZE      100

   	printf("test\n");

   	int *host_buf = (int *)malloc(BUF_SIZE);
    int *dev_buf = NULL;
	CU_CHECK(cudaMalloc((void **)&dev_buf, BUF_SIZE));
	CU_CHECK(cudaMemset(dev_buf, 0, BUF_SIZE));

   	dim3 dimGrid(1);
	dim3 dimBlock(1, 1, 1);

	cooperative_kernel<<<dimGrid, dimBlock>>>(dev_buf);
	CU_CHECK(cudaDeviceSynchronize());

	host_buf[0] = 100;
	CU_CHECK(cudaMemcpy(host_buf, dev_buf, BUF_SIZE, cudaMemcpyDeviceToHost));

	printf("%d\n", host_buf[0]);
}






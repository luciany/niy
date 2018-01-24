void test(){
	cudaError_t err = cudaSuccess;
	cudaDeviceProp prop;
	int count = 0;

	int version;
	CU_CHECK(cudaRuntimeGetVersion(&version));
	printf("cudaRuntimeGetVersion %d\n", version);
	CU_CHECK(cudaDriverGetVersion(&version));
	printf("cudaDriverGetVersion %d\n", version);

	cudaGetDeviceCount(&count);

	for (int i = 0; i < count; i++) {
		printf("Device %d\n", i);
		prop.totalGlobalMem = 0;
		err = cudaGetDeviceProperties(&prop, i);
		CU_CHECK(err);

		printf("  name: %s\n", prop.name);
		printf("  major.minor: %d.%d\n", prop.major, prop.minor);
		printf("  clockRate: %d\n", prop.clockRate);
		printf("  deviceOverlap: %d\n", prop.deviceOverlap);
		printf("  kernelExecTimeoutEnabled: %d\n", prop.kernelExecTimeoutEnabled);
		printf("  integrated: %d\n", prop.integrated);
		printf("\n");
		printf("  totalGlobalMem: %lld\n", prop.totalGlobalMem);
		printf("  totalConstMem: %ld\n", prop.totalConstMem);
		printf("  memPitch: %ld\n", prop.memPitch);
		printf("  textureAlignment: %ld\n", prop.textureAlignment);
		printf("\n");
		printf("  multiProcessorCount: %d\n", prop.multiProcessorCount);
		printf("  sharedMemPerBlock: %ld\n", prop.sharedMemPerBlock);
		printf("  regsPerBlock: %d\n", prop.regsPerBlock);
		printf("  warpSize: %d\n", prop.warpSize);
		printf("  maxThreadsPerBlock: %d\n", prop.maxThreadsPerBlock);
		printf("  maxThreadsDim: %d  %d  %d\n", 
			prop.maxThreadsDim[0], prop.maxThreadsDim[1], prop.maxThreadsDim[2]);
		printf("  maxGridSize: %d  %d  %d\n", 
			prop.maxGridSize[0], prop.maxGridSize[1], prop.maxGridSize[2]);
		printf("\n");
	}
}




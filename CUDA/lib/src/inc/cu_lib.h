#pragma once

#ifdef __cplusplus
extern "C" {
#endif

#define cu_check(err) do {\
	if (err != cudaSuccess) {\
		fprintf(stderr, "\n---------------- ERROR ----------------\n--  %s\n", cudaGetErrorString(err));\
		fprintf(stderr, "--  %s: %d\n", __FILE__, __LINE__);\
		exit(EXIT_FAILURE);\
	}\
} while(0)

void cu_device_prop();

#ifdef __cplusplus
}
#endif

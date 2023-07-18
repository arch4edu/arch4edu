#include <hip/hip_runtime.h>
#include <cstdio>

__global__ void vector_add(double *out, double *a, double *b, int n)
{
  size_t index = blockIdx.x * blockDim.x + threadIdx.x;
  size_t stride = blockDim.x * gridDim.x;

  for (size_t i = index; i < n; i += stride)
    out[i] = a[i] + b[i];
}

extern "C"
{
  void launch(dim3* grid, dim3* block, int shmem, hipStream_t stream, double *dout, double *da, double *db, int N)
  {
    //printf("launching kernel\n");
    hipLaunchKernelGGL((vector_add), *grid, *block, shmem, stream, dout, da, db, N);
  }
}

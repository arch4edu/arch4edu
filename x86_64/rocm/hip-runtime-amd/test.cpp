#include <iostream>
#include <cmath>
#include <vector>
#include <hip/hip_runtime.h>

__global__
void saxpy(int n, float a, const float *x, float *y)
{
    int i = hipThreadIdx_x + hipBlockDim_x * hipBlockIdx_x;
    if(i < n){
        y[i] = a * x[i] + y[i];
    }
}

__global__
void sset(int n, float a, float *x)
{
    int i = hipThreadIdx_x + hipBlockDim_x * hipBlockIdx_x;
    if(i < n){
        x[i] = a;
    }
}

int main()
{
    hipDeviceProp_t prop;
    hipGetDeviceProperties(&prop, 0);
    std::cout << "Agent " << prop.name << "\n";
    std::cout << "System version " << prop.major
        << "." << prop.minor << "\n";

    int n = 1024;
    float *x;
    float *y;
    hipMalloc((void**)&x, sizeof *x * n);
    hipMalloc((void**)&y, sizeof *y * n);

    std::vector<float> xin(n);
    for(int i = 0; i < n; i++){
        xin[i] = -1.0 + 2.0 * i / n;
    }
    hipMemcpy(x, xin.data(), sizeof *x * n, hipMemcpyHostToDevice);

    float ac = -14.412f;
    hipLaunchKernelGGL(sset, dim3(1), dim3(n), 0, 0, n, ac, y);

    float a = 5321.124f;
    hipLaunchKernelGGL(saxpy, dim3(1), dim3(n), 0, 0, n, a, x, y);

    std::vector<float> yout(n);
    hipMemcpy(yout.data(), y, sizeof *y * n, hipMemcpyDeviceToHost);

    hipFree(x);
    hipFree(y);

    for(int i = 0; i < n; i++){
        yout[i] -= a * xin[i];
        if(std::abs(yout[i] - ac) > 0.001f){
            std::cout << "Test failed at index " << i
                << " with entry " << yout[i]
                << " (" << ac << ")\n";
            return 1;
        }
    }
    std::cout << "TESTS PASSED!" << std::endl;
}

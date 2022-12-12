#include <rocblas/rocblas.h>
#include <hip/hip_runtime.h>
#include <vector>
#include <random>
#include <algorithm>
#include <cmath>
#include <iostream>

int main()
{
    size_t n = 128;
    size_t size = n * n;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dist(-1.0, 1.0);
    auto myrand = [&](){return dist(gen);};

    float *x;
    float *y;
    float *z;
    hipMalloc((void**)&x, sizeof *x * size);
    hipMalloc((void**)&y, sizeof *y * size);
    hipMalloc((void**)&z, sizeof *z * size);

    std::vector<float> xin(size);
    std::vector<float> yin(size);

    std::generate(xin.begin(), xin.end(), myrand);
    std::generate(yin.begin(), yin.end(), myrand);

    hipMemcpy(x, xin.data(), sizeof *x * size, hipMemcpyHostToDevice);
    hipMemcpy(y, yin.data(), sizeof *x * size, hipMemcpyHostToDevice);

    rocblas_handle handle;
    rocblas_create_handle(&handle);

    float alpha = 15.412f;
    float beta = 0.0f;
    rocblas_sgemm(handle, rocblas_operation_none, rocblas_operation_none,
        n, n, n, &alpha, x, n, y, n, &beta, z, n);

    std::vector<float> zout(size);
    hipMemcpy(zout.data(), z, sizeof *z * size, hipMemcpyDeviceToHost);

    for(size_t j = 0; j < n; j++){
        for(size_t i = 0; i < n; i++){
            for(size_t k = 0; k < n; k++){
                zout[i + j * n] -= alpha * xin[i + k * n] * yin[k + j * n];
            }
        }
    }

    float tol = 0.001f;
    for(size_t i = 0; i < size; i++){
        if(std::abs(zout[i]) > tol){
            std::cout << "Element mismatch at index " << i << "\n";
            std::cout << "Expected: 0\n";
            std::cout << "Actual  : " << zout[i] << "\n";
            return 1;
        }
    }

    std::cout << "TESTS PASSED!" << std::endl;

    hipFree(x);
    hipFree(y);
    hipFree(z);
    rocblas_destroy_handle(handle);
}

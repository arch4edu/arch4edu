#include <rocsolver/rocsolver.h>
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

    float *a;
    float *x;
    hipMalloc((void**)&a, sizeof *a * size);
    hipMalloc((void**)&x, sizeof *x * n);

    std::vector<float> ain(size);
    std::vector<float> xin(n);
    std::generate(ain.begin(), ain.end(), myrand);
    std::generate(xin.begin(), xin.end(), myrand);

    hipMemcpy(a, ain.data(), sizeof *a * size, hipMemcpyHostToDevice);
    hipMemcpy(x, xin.data(), sizeof *x * n, hipMemcpyHostToDevice);

    rocblas_handle handle;
    rocblas_create_handle(&handle);

    rocblas_int *info;
    hipMalloc((void**)&info, sizeof *info);
    rocsolver_sgels(handle, rocblas_operation_none,
        n, n, 1, a, n, x, n, info);

    std::vector<float> xout(n);
    hipMemcpy(xout.data(), x, sizeof *x * n, hipMemcpyDeviceToHost);
    rocblas_int hinfo;
    hipMemcpy(&hinfo, info, sizeof *info, hipMemcpyDeviceToHost);

    if(hinfo != 0){
        std::cout << "Matrix is rank deficient!\n";
        return 1;
    }

    float tol = 0.001f;
    for(size_t i = 0; i < n; i++){
        for(size_t j = 0; j < n; j++){
            xin[i] -= ain[i + j * n] * xout[j];
        }
        if(std::abs(xin[i]) > tol){
            std::cout << "Missmatch at index " << i << "\n"
                << "Desired: 0" << "\n"
                << "Actual : " << xin[i] << std::endl;
            return 1;
        }
    }

    std::cout << "TESTS PASSED!" << std::endl;

    hipFree(a);
    hipFree(x);
    rocblas_destroy_handle(handle);
}

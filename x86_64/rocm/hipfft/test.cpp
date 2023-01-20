#include <hipfft/hipfft.h>
#include <hip/hip_runtime.h>
#include <vector>
#include <numeric>
#include <cmath>
#include <iostream>

int main()
{
    size_t size = 1024 * 1024;

    hipfftComplex *x;
    hipMalloc((void**)&x, sizeof *x * size);

    std::vector<hipfftComplex> xin(size);
    for(auto &xx: xin){
        xx.x = 1.0f;
        xx.y = 0.0f;
    }
    hipMemcpy(x, xin.data(), sizeof *x * size, hipMemcpyHostToDevice);

    hipfftHandle plan;
    hipfftPlan1d(&plan, size, HIPFFT_C2C, 1);

    hipfftExecC2C(plan, x, x, HIPFFT_FORWARD);

    std::vector<hipfftComplex> xout(size);
    hipMemcpy(xout.data(), x, sizeof *x * size, hipMemcpyDeviceToHost);

    std::vector<hipfftComplex> xref(size);
    for(auto &xx: xref){
        xx.x = 0.0f;
        xx.y = 0.0f;
    }
    xref[0].x = 1.0f * size;
    
    float tol = 0.001f;
    for(size_t i = 0; i < size; i++){
        if(std::abs(xref[i].x - xout[i].x) + std::abs(xref[i].y - xout[i].y) > tol){
            std::cout << "Element mismatch at index " << i << "\n";
            std::cout << "Expected: " << xref[i].x << " " << xref[i].y << "\n";
            std::cout << "Actual  : " << xout[i].x << " " << xout[i].y << "\n";
            return 1;
        }
    }

    std::cout << "TESTS PASSED!" << std::endl;

    hipFree(x);
    hipfftDestroy(plan);
}

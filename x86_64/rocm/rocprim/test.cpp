#include <rocprim/rocprim.hpp>
#include <vector>
#include <iostream>
#include <random>
#include <algorithm>
#include <cmath>

int main()
{
    auto xpy = [] __device__(float x, float y) -> float{
        return x + y;
    };

    size_t size = 1024;
    std::vector<float> xin(size);
    std::vector<float> yin(size);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dist(-1.0, 1.0);

    auto myrand = [&]() -> float {return dist(gen);};

    std::generate(xin.begin(), xin.end(), myrand);
    std::generate(yin.begin(), yin.end(), myrand);

    std::vector<float> zref(size);
    for(size_t i = 0; i < size; i++){
        zref[i] = xin[i] + yin[i];
    }

    float *x;
    float *y;
    float *z;
    hipMalloc((void**)&x, sizeof *x * size);
    hipMalloc((void**)&y, sizeof *y * size);
    hipMalloc((void**)&z, sizeof *z * size);

    hipMemcpy(x, xin.data(), sizeof *x * size, hipMemcpyHostToDevice);
    hipMemcpy(y, yin.data(), sizeof *y * size, hipMemcpyHostToDevice);

    rocprim::transform(x, y, z, size, xpy);

    std::vector<float> zout(size);
    hipMemcpy(zout.data(), z, sizeof *z * size, hipMemcpyDeviceToHost);

    for(size_t i = 0; i < size; i++){
        if(std::abs(zout[i] - zref[i]) > 0.001f){
            std::cout << "Element mismatch at index " << i << "\n";
            std::cout << "Got " << zout[i] << " but expected " << zref[i] << "\n";
            return 1;
        }
    }
    std::cout << "TESTS PASSED!" << std::endl;

    hipFree(x);
    hipFree(y);
    hipFree(z);
}

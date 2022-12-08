#include <thrust/copy.h>
#include <thrust/host_vector.h>
#include <thrust/device_vector.h>
#include <thrust/sort.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

int main(int argc, char *argv[])
{
    size_t size = 1024;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dist(-1.0, 1.0);

    auto myrand = [&]() -> float {return dist(gen);};

    thrust::host_vector<float> xin(size);
    std::generate(xin.begin(), xin.end(), myrand);

    thrust::device_vector<float> x(size);
    x = xin;

    thrust::sort(x.begin(), x.end());
    thrust::copy(x.begin(), x.end(), xin.begin());

    for(size_t i = 1; i < size; i++){
        if(xin[i - 1] > xin[i]){
            std::cout << "Elements " << i - 1 << " and " << i
                << "are not sorted:\n";
            std::cout << xin[i - 1] << " " << xin[i] << std::endl;
            return 1;
        }
    }

    std::cout << "TESTS PASSED!" << std::endl;
}

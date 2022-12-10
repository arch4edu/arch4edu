#include <rocfft/rocfft.h>
#include <hip/hip_runtime.h>
#include <hip/hip_vector_types.h>
#include <vector>
#include <numeric>
#include <cmath>
#include <iostream>

int main()
{
    size_t size = 1024 * 1024;

    rocfft_setup();

    float2 *x;
    hipMalloc((void**)&x, sizeof *x * size);


    std::vector<float2> xin(size);
    for(auto &xx: xin){
        xx.x = 1.0f;
        xx.y = 0.0f;
    }
    hipMemcpy(x, xin.data(), sizeof *x * size, hipMemcpyHostToDevice);

    rocfft_plan plan = nullptr;
    size_t len = size;
    rocfft_plan_create(&plan, rocfft_placement_inplace,
        rocfft_transform_type_complex_forward, rocfft_precision_single,
        1, &len, 1, nullptr);
    size_t work_size = 0;
    rocfft_plan_get_work_buffer_size(plan, &work_size);
    void *work;
    rocfft_execution_info info = nullptr;
    if(work_size){
        rocfft_execution_info_create(&info);
        hipMalloc((void**)&work, work_size);
        rocfft_execution_info_set_work_buffer(info, work, work_size);
    }
    rocfft_execute(plan, (void**)&x, nullptr, info);

    std::vector<float2> xout(size);
    hipMemcpy(xout.data(), x, sizeof *x * size, hipMemcpyDeviceToHost);

    std::vector<float2> xref(size);
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
    rocfft_plan_destroy(plan);
    rocfft_cleanup();
}

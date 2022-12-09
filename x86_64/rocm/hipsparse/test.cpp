#include <hipsparse/hipsparse.h>
#include <hip/hip_runtime.h>
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

int main()
{
    int n = 1024;

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dist(-1.0, 1.0);

    auto myrand = [&]() -> float {return dist(gen);};

    std::vector<float> xin(n);
    std::generate(xin.begin(), xin.end(), myrand);

    hipsparseHandle_t handle;
    hipsparseCreate(&handle);

    std::vector<int> row_ptr(n + 1);
    std::vector<int> col(3 * n);
    std::vector<float> data(3 * n);
    
    //Second order finite differences matrix in 1D
    row_ptr[0] = 0;
    for(size_t i = 0; i < n; i++){
        int off = row_ptr[i];
        if(i > 0){
            col[off] = i - 1;
            data[off++] = -1.0f;
        }
        col[off] = i;
        data[off++] = 2.0f;
        if(i < n - 1){
            col[off] = i + 1;
            data[off++] = -1.0f;
        }
        row_ptr[i + 1] = off;
    }

    int *rp;
    int *c;
    float *d;

    float *x;
    float *y;
    hipMalloc((void **)&rp, sizeof *rp * (n + 1));
    hipMalloc((void **)&c, sizeof *c * 3 * n);
    hipMalloc((void **)&d, sizeof *d * 3 * n);

    hipMalloc((void **)&x, sizeof *x * n);
    hipMalloc((void **)&y, sizeof *y * n);

    hipMemcpy(rp, row_ptr.data(), sizeof *rp * (n + 1), hipMemcpyHostToDevice);
    hipMemcpy(c, col.data(), sizeof *c * 3 * n, hipMemcpyHostToDevice);
    hipMemcpy(d, data.data(), sizeof *d * 3 * n, hipMemcpyHostToDevice);

    hipMemcpy(x, xin.data(), sizeof *x * n, hipMemcpyHostToDevice);

    float alpha = 14.124f;
    float beta = 0.0f;

    hipsparseMatDescr_t descr;
    hipsparseCreateMatDescr(&descr);

    hipsparseScsrmv(handle, HIPSPARSE_OPERATION_NON_TRANSPOSE,
        n, n, 3 * n - 2, &alpha, descr, d, rp, c,
        x, &beta, y);

    std::vector<float> yout(n);
    hipMemcpy(yout.data(), y, sizeof *y * n, hipMemcpyDeviceToHost);

    float tol = 0.0001f;
    for(int i = 0; i < n; i++){
        for(int jj = row_ptr[i]; jj < row_ptr[i + 1]; jj++){
            int j = col[jj];
            yout[i] -= alpha * data[jj] * xin[j];
        }
        if(std::abs(yout[i]) > tol){
            std::cout << "Entry " << i << " is not computed correctly.\n";
            std::cout << "Expected 0 but got " <<  yout[i] << std::endl;
            return 1;
        }
    }

    std::cout << "TESTS PASSED!" << std::endl;

    hipsparseDestroy(handle);
    hipsparseDestroyMatDescr(descr);
    hipFree(rp);
    hipFree(c);
    hipFree(d);
    hipFree(x);
    hipFree(y);
}

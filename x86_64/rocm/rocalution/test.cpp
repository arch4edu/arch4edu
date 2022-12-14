#include <rocalution/rocalution.hpp>
#include <vector>
#include <iostream>

using namespace rocalution;

int main()
{
    init_rocalution();
    info_rocalution();
    size_t n = 128;


    float *data = new float[3 * n];
    int *row_ptr = new int[n + 1];
    int *col = new int[3 * n];
    row_ptr[0] = 0;
    int off;
    for(int i = 0; i < n; i++){
        off = row_ptr[i];
        if(i > 0){
            data[off] = -1.0;
            col[off++] = i - 1;
        }
        data[off] = 2.0;
        col[off++] = i;
        if(i < n - 1){
            data[off] = -1.0;
            col[off++] = i + 1;
        }
        row_ptr[i + 1] = off;
    }

    
    LocalVector<float> x;
    LocalVector<float> b;
    LocalVector<float> r;
    LocalMatrix<float> A;

    A.SetDataPtrCSR(&row_ptr, &col, &data,
        "matrix", row_ptr[n], n, n);
    A.Check();

    A.MoveToAccelerator();
    x.MoveToAccelerator();
    b.MoveToAccelerator();
    r.MoveToAccelerator();

    x.Allocate("x", n);
    b.Allocate("b", n);
    r.Allocate("r", n);

    CG<LocalMatrix<float>, LocalVector<float>, float> ls;

    b.SetRandomUniform(2342359);
    x.Zeros();
    r.CopyFrom(b);

    A.Info();

    ls.InitTol(1e-6, 5e-4, 1e3);
    ls.SetOperator(A);

    ls.Build();
    ls.Verbose(1);

    ls.Solve(b, &x);

    A.Apply(x, &r);

    r.ScaleAdd(-1.0, b);

    float nrm = r.Norm();
    float tol = 0.001f;
    if(nrm > tol){
        std::cout << "Solver failed with tolerance " << tol << std::endl;
        return 1;
    }
    
    std::cout << "TESTS PASSED!" << std::endl;

    stop_rocalution();
}

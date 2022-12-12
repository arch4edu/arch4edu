# Maintainer: Torsten Keßler <t dot kessler at posteo dot de>

pkgbase=rocm-hip-sdk
pkgname=(rocm-hip-sdk
         rocm-hip-libraries
         rocm-openmp-sdk
         rocm-opencl-sdk
         rocm-hip-runtime
         rocm-language-runtime
         rocm-ml-sdk
         rocm-ml-libraries
         rocm-developer-tools)
pkgver=5.4.0
pkgrel=1
arch=('x86_64')
license=('None')
url='https://docs.amd.com/'

package_rocm-hip-sdk() {
    pkgdesc='Develop applications using HIP and libraries for AMD platforms'
    depends=('rocm-hip-libraries'
             'rocm-llvm'
             'rocm-core'
             'rocm-hip-runtime'
             'hipblas'
             'hipcub'
             'hipfft'
             'hipsparse'
             'hipsolver'
             'miopen-hip'
             'rccl'
             'rocalution'
             'rocblas'
             'rocfft'
             'rocprim'
             'rocrand'
             'rocsolver'
             'rocsparse'
             'rocthrust')
}

package_rocm-hip-libraries() {
    pkgdesc='Develop certain applications using HIP and libraries for AMD platforms'
    depends=('rocm-core'
             'rocm-hip-runtime'
             'hipblas'
             'hipfft'
             'hipsparse'
             'hipsolver'
             'rccl'
             'rocalution'
             'rocblas'
             'rocfft'
             'rocrand'
             'rocsolver'
             'rocsparse')
}

package_rocm-openmp-sdk() {
    pkgdesc='Develop OpenMP-based applications for AMD platforms'
    depends=('rocm-core'
             'rocm-llvm'
             'openmp-extras'
             'rocm-language-runtime')
}

package_rocm-opencl-sdk() {
    pkgdesc='Develop OpenCL-based applications for AMD platforms'
    depends=('rocm-core'
             'hsa-rocr'
             'rocm-opencl-runtime'
             'hsakmt-roct')
}

package_rocm-hip-runtime() {
    pkgdesc='Packages to run HIP applications on the AMD platform'
    depends=('rocm-core'
             'rocm-language-runtime'
             'rocminfo'
             'hip-runtime-amd'
             'rocm-llvm'
             'rocm-cmake')
}

package_rocm-language-runtime() {
    pkgdesc='ROCm runtime'
    depends=('rocm-core'
             'hsakmt-roct'
             'hsa-rocr'
             'rocm-device-libs'
             'comgr')
}

package_rocm-ml-sdk() {
    pkgdesc='develop and run Machine Learning applications optimized for AMD platforms'
    depends=('rocm-core'
             'rocm-hip-sdk'
             'rocm-ml-libraries'
             'miopen-hip')
}

package_rocm-ml-libraries() {
    pkgdesc='Packages for key Machine Learning libraries'
    depends=('rocm-core'
             'rocm-hip-libraries'
             'rocm-llvm'
             'miopen-hip')
}

package_rocm-developer-tools() {
    pkgdesc='Packages required to debug and profile HIP-based applications'
    depends=('rocm-core'
             'rocm-hip-sdk'
             'hsa-amd-aqlprofile'
             'rocprofiler'
             'roctracer'
             'rocm-gdb'
             'rocm-dbgapi'
             'rocm-debug-agent')
}

# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

_benchver=1.1.0
_cnmemver=1.0.0
_cubver=1.6.4
_eigenver=3.3.3
_gtestver=1.8.0
_ncclver=1.3.4-1
_protover=3.3.1
_pybindver=2.1.1
_gitver=gitmaster
_gitwebver=master

pkgname=caffe2
pkgver=0.7.0
pkgrel=6
pkgdesc="A new lightweight, modular, and scalable deep learning framework (gpu enabled)"
arch=('x86_64')
url="http://caffe2.ai/"
license=('BSD')
depends=(
    # binary repositories:
        # required:
            'google-glog' 'protobuf' 'python2' 'python2-numpy' 'python2-protobuf' 'cuda'
            'cudnn'
        # not required but enabled in build:
            'gflags' 'gtest' 'openmp' 'leveldb' 'lmdb' 'opencv' 'openmpi' 'snappy'
            'zeromq' 'hiredis'
        # python2:
            'python2-pydot' 'python2-flask' 'graphviz' 'python2-hypothesis'
            'python2-jupyter_core' 'python2-matplotlib' 'python2-yaml' 'python2-requests'
            'python2-scipy' 'python2-setuptools' 'python2-tornado' 'python2-pyzmq'
            'python2-gflags'
    # AUR:
        # not required but enabled in build:
            'nccl'
        # python2:
            'python2-scikit-image' 'python2-leveldb' 'python2-lmdb' 'python2-glog'
    # missing:
        # 'python2-nvd3'
)
makedepends=('cmake' 'gcc5')
conflicts=('caffe' 'caffe-cpu' 'caffe-git' 'caffe-cpu-git'
           'caffe2-git' 'caffe2-cpu' 'caffe2-cpu-git')
options=('!emptydirs')
source=(
    # main source:
        "${pkgname}-${pkgver}.tar.gz"::"https://github.com/${pkgname}/${pkgname}/archive/v${pkgver}.tar.gz"
    # third party:
        "thirdparty-android-cmake-${_gitver}.zip"::"https://github.com/taka-no-me/android-cmake/archive/${_gitwebver}.zip"
        "thirdparty-benchmark-${_benchver}.tar.gz"::"https://github.com/google/benchmark/archive/v${_benchver}.tar.gz"
        "thirdparty-cnmem-${_cnmemver}.tar.gz"::"https://github.com/NVIDIA/cnmem/archive/v${_cnmemver}.tar.gz"
        "thirdparty-cub-${_cubver}.zip"::"https://github.com/NVlabs/cub/archive/${_cubver}.zip"
        "thirdparty-eigen-${_eigenver}.tar.gz"::"https://github.com/RLovelett/eigen/archive/${_eigenver}.tar.gz"
        "thirdparty-gloo-${_gitver}.zip"::"https://github.com/facebookincubator/gloo/archive/${_gitwebver}.zip"
        "thirdparty-googletest-${_gtestver}.tar.gz"::"https://github.com/google/googletest/archive/release-${_gtestver}.tar.gz"
        "thirdparty-ios-cmake-${_gitver}.zip"::"https://github.com/Yangqing/ios-cmake/archive/${_gitwebver}.zip"
        "thirdparty-nccl-${_ncclver}.tar.gz"::"https://github.com/NVIDIA/nccl/archive/v${_ncclver}.tar.gz"
        "thirdparty-nervanagpu-${_gitver}.zip"::"https://github.com/NervanaSystems/nervanagpu/archive/${_gitwebver}.zip"
        "thirdparty-NNPACK-${_gitver}.zip"::"https://github.com/Maratyszcza/NNPACK/archive/${_gitwebver}.zip"
        "thirdparty-protobuf-${_protover}.tar.gz"::"https://github.com/google/protobuf/archive/v${_protover}.tar.gz"
        "thirdparty-pybind11-${_pybindver}.tar.gz"::"https://github.com/pybind/pybind11/archive/v${_pybindver}.tar.gz"
        "thirdparty-FP16-${_gitver}.zip"::"https://github.com/Maratyszcza/FP16/archive/${_gitwebver}.zip"
        "thirdparty-FXdiv-${_gitver}.zip"::"https://github.com/Maratyszcza/FXdiv/archive/${_gitwebver}.zip"
        "thirdparty-psimd-${_gitver}.zip"::"https://github.com/Maratyszcza/psimd/archive/${_gitwebver}.zip"
        "thirdparty-pthreadpool-${_gitver}.zip"::"https://github.com/Maratyszcza/pthreadpool/archive/${_gitwebver}.zip"
)
noextract=("thirdparty-android-cmake-${_gitver}.zip"
           "thirdparty-benchmark-${_benchver}.tar.gz"
           "thirdparty-cnmem-${_cnmemver}.tar.gz"
           "thirdparty-cub-${_cubver}.zip"
           "thirdparty-eigen-${_eigenver}.tar.gz"
           "thirdparty-gloo-${_gitver}.zip"
           "thirdparty-googletest-${_gtestver}.tar.gz"
           "thirdparty-ios-cmake-${_gitver}.zip"
           "thirdparty-nccl-${_ncclver}.tar.gz"
           "thirdparty-nervanagpu-${_gitver}.zip"
           "thirdparty-NNPACK-${_gitver}.zip"
           "thirdparty-protobuf-${_protover}.tar.gz"
           "thirdparty-pybind11-${_pybindver}.tar.gz"
           "thirdparty-FP16-${_gitver}.zip"
           "thirdparty-FXdiv-${_gitver}.zip"
           "thirdparty-psimd-${_gitver}.zip"
           "thirdparty-pthreadpool-${_gitver}.zip"
)
sha256sums=('b8f266ed283efc172fa96c06c878ed7f125755f89cde480580b754c1f03c0bab'
            'SKIP'
            'e7334dd254434c6668e33a54c8f839194c7c61840d52f4b6258eee28e9f3b20e'
            'bd8c2803813f00c55995b106a5d385a343211100f8943856525472997f5b2bb0'
            '966d0c4f41e2bdc81aebf9ccfbf0baffaac5a74f00b826b06f4dee79b2bb8cee'
            '1b7e1dba81c0de7267437e91be9508e80ced48b7ba5b58847eac7dafc1b89acc'
            'SKIP'
            '58a6f4277ca2bc8565222b3bbd58a177609e9c488e8a72649359ba51450db7d8'
            'SKIP'
            '11e4eb44555bb28b9cbad973dacb4640b82710c9769e719afc2013b63ffaf884'
            'SKIP'
            'SKIP'
            '30f23a45c6f4515598702a6d19c4295ba92c4a635d7ad8d331a4db9fccff392d'
            'f2c6874f1ea5b4ad4ffffe352413f7d2cd1a49f9050940805c2a082348621540'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
)

prepare() {
    cd "${pkgname}-${pkgver}/third_party"
    
    _thirdparty_list="android-cmake benchmark cnmem cub eigen gloo googletest
                     ios-cmake nccl nervanagpu NNPACK protobuf pybind11"
    _nnpackdeps_list="FP16 FXdiv psimd pthreadpool"
    
    for _component in $_thirdparty_list
    do
        cd "$_component"
        bsdtar -xf "${srcdir}/thirdparty-${_component}"* -s'|[^/]*/||'
        cd ..
    done
    
    cd NNPACK_deps
    for _component in $_nnpackdeps_list
    do
        cd "$_component"
        bsdtar -xf "${srcdir}/thirdparty-${_component}"* -s'|[^/]*/||'
        cd ..
    done
}

build() {
    cd "${pkgname}-${pkgver}"
    mkdir -p build
    cd build
    
    cmake \
        -DBLAS:STRING=Eigen \
        \
        -DBUILD_BINARY:BOOL=ON \
        -DBUILD_PYTHON:BOOL=ON \
        -DBUILD_SHARED_LIBS:BOOL=ON \
        \
        -DBUILD_TEST:BOOL=OFF \
        \
        -DCAFFE2_CPU_FLAGS:BOOL=OFF \
        -DCMAKE_BUILD_TYPE:STRING=Release \
        -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
        -DCMAKE_CXX_COMPILER=/usr/bin/g++-5 \
        -DCMAKE_C_COMPILER=/usr/bin/gcc-5 \
        -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=NO \
        -DCMAKE_SKIP_RPATH:BOOL=NO \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=FALSE \
        \
        -DCUDA_64_BIT_DEVICE_CODE:BOOL=ON \
        -DCUDA_ARCH_NAME:STRING=Auto \
        -DCUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE:BOOL=ON \
        -DCUDA_BUILD_CUBIN:BOOL=OFF \
        -DCUDA_BUILD_EMULATION:BOOL=OFF \
        -DCUDA_HOST_COMPILATION_CPP:BOOL=ON \
        -DCUDA_HOST_COMPILER:FILEPATH=/usr/bin/gcc-5 \
        -DCUDA_NVCC_EXECUTABLE:FILEPATH=/opt/cuda/bin/nvcc \
        -DCUDA_PROPAGATE_HOST_FLAGS:BOOL=ON \
        -DCUDA_SDK_ROOT_DIR:PATH=/opt/cuda \
        -DCUDA_SEPARABLE_COMPILATION:BOOL=OFF \
        -DCUDA_TOOLKIT_INCLUDE:PATH=/opt/cuda/include \
        -DCUDA_TOOLKIT_ROOT_DIR:PATH=/opt/cuda \
        -DCUDA_USE_STATIC_CUDA_RUNTIME:BOOL=OFF \
        -DCUDA_VERBOSE_BUILD:BOOL=OFF \
        -DCUDA_VERSION:STRING=8.0 \
        -DCUDNN_INCLUDE_DIR:PATH=/opt/cuda/include \
        -DCUDNN_ROOT_DIR:PATH=/opt/cuda \
        \
        -DGLOO_STATIC_OR_SHARED:STRING=STATIC \
        -DNCCL_INCLUDE_DIR:PATH=/opt/cuda/include \
        -DNCCL_LIBRARY:FILEPATH=/opt/cuda/lib64/libnccl.so \
        -DNCCL_ROOT_DIR:PATH=/opt/cuda \
        \
        -DOpenCV_DIR:PATH=/usr/share/OpenCV \
        \
        -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python2.7 \
        -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python2.7 \
        -DPYTHON_LIBRARY:FILEPATH=/usr/lib/libpython2.7.so \
        \
        -DUSE_CNMEM:BOOL=OFF \
        -DUSE_CUDA:BOOL=ON \
        -DUSE_GFLAGS:BOOL=ON \
        -DUSE_GLOG:BOOL=ON \
        -DUSE_GLOO:BOOL=ON \
        -DUSE_LEVELDB:BOOL=ON \
        -DUSE_LITE_PROTO:BOOL=OFF \
        -DUSE_LMDB:BOOL=ON \
        -DUSE_MPI:BOOL=ON \
        -DUSE_NCCL:BOOL=ON \
        -DUSE_NERVANA_GPU:BOOL=ON \
        -DUSE_NNPACK:BOOL=OFF \
        -DUSE_OPENCV:BOOL=ON \
        -DUSE_OPENMP:BOOL=ON \
        -DUSE_REDIS:BOOL=ON \
        -DUSE_ROCKSDB:BOOL=OFF \
        -DUSE_THREADS:BOOL=ON \
        -DUSE_ZMQ:BOOL=ON \
        \
        -Wno-dev \
        ..
        
    # NOTE:
    # The recommended approach of running make in build() and make install in
    # package() produces two compilations (being the second one unnecessary).
    # A workaround is to suppress make in build() and run only make install
    # in package().
    
    #make
}

package() {
    cd "${pkgname}-${pkgver}/build"
    make DESTDIR="$pkgdir" install
    
    # directories creation
    mkdir -p "${pkgdir}/usr/lib/python2.7/site-packages"
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    
    # move/rename folders to the right location
    mv -f "${pkgdir}/usr/binaries" "${pkgdir}/usr/bin"
    mv -f "${pkgdir}/usr/caffe"    "${pkgdir}/usr/lib/python2.7/site-packages"
    mv -f "${pkgdir}/usr/caffe2"   "${pkgdir}/usr/lib/python2.7/site-packages"
    
    # license
    cd "${srcdir}/${pkgname}-${pkgver}"
    install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 "PATENTS" "${pkgdir}/usr/share/licenses/${pkgname}/PATENTS"
}

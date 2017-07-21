# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

# third_party with no stable release at the needed commit
_android_cmake_commit='556cc14296c226f753a3778d99d8b60778b7df4f'
_benchmark_commit='4bf28e611b55de8a2d4eece3c335e014f8b0f630'
_cnmem_commit='28a182d49529da49f4ac4e3941cec3edf16b3540'
_cub_commit='89de7ab20167909bc2c4f8acd397671c47cf3c0d'
_gloo_commit='f67ab32d3439061946ce2c1bed8baa0e1b5d367f'
_googletest_commit='5e7fd50e17b6edf1cadff973d0ec68966cf3265e'
_ios_cmake_commit='e3a7695d1d68ef4eca716031f94e8475b1589b1f'
_nccl_commit='2a974f5ca2aa12b178046b2206b43f1fd69d9fae'
_nervanagpu_commit='d4eefd50fbd7d34a17dddbc829888835d67b5f4a'
_nnpack_commit='02bfa475d64040cd72b7c01daa9e862523ae87da'
_pybind11_commit='f38f359f96815421f1780c1a676715efd041f1ae'
_nnpackdeps_fp16_commit='2e9eeeb0b463736d13b887d790ac7e72e78fa4bc'
_nnpackdeps_fxdiv_commit='8f85044fb41e560508cd69ed26c9afb9cc120e8a'
_nnpackdeps_psimd_commit='0b26a3fb98dd6af7e1f4e0796c56df6b32b1c016'
_nnpackdeps_pthreadpool_commit='9e17903a3fc963fe86b151aaddae7cf1b1d34815'

 # third_party with stable release at the needed commit
_eigen_version='3.3.2'    # commit 'ae9889a130bd0a9d3007f41d015563c2e8ac605f' is version '3.3.2'
_protobuf_version='3.1.0' # commit 'a428e42072765993ff674fda72863c9f1aa2d268' is version '3.1.0'

pkgname=caffe2
pkgver=0.7.0
pkgrel=13
pkgdesc='A new lightweight, modular, and scalable deep learning framework (gpu enabled)'
arch=('x86_64')
url='http://caffe2.ai/'
license=('BSD')
depends=(
    # official repositories:
        # required:
            'google-glog' 'protobuf' 'python2' 'python2-numpy' 'python2-protobuf' 'cuda'
            'cudnn'
        # not required but enabled in build:
            'gflags' 'gtest' 'openmp' 'leveldb' 'lmdb' 'openmpi' 'snappy' 'zeromq'
            'hiredis'
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
makedepends=(
    # official repositories:
        'git' 'cmake' 'gcc5' 'ninja'
    # AUR:
        'confu-git' 'python-peachpy-git'
)
conflicts=('caffe' 'caffe-cpu' 'caffe-git' 'caffe-cpu-git'
           'caffe2-git' 'caffe2-cpu' 'caffe2-cpu-git')
options=('!emptydirs')
source=(
    # main source:
        "${pkgname}-${pkgver}.tar.gz"::"https://github.com/${pkgname}/${pkgname}/archive/v${pkgver}.tar.gz"
        'external-nnpack-fix.patch'
    # third party:
        'thirdparty-android-cmake-git'::"git+https://github.com/taka-no-me/android-cmake.git#commit=${_android_cmake_commit}"
        'thirdparty-benchmark-git'::"git+https://github.com/google/benchmark.git#commit=${_benchmark_commit}"
        'thirdparty-cnmem-git'::"git+https://github.com/NVIDIA/cnmem.git#commit=${_cnmem_commit}"
        'thirdparty-cub-git'::"git+https://github.com/NVlabs/cub.git#commit=${_cub_commit}"
        "thirdparty-eigen-${_eigen_version}.tar.gz"::"https://github.com/RLovelett/eigen/archive/${_eigen_version}.tar.gz"
        'thirdparty-gloo-git'::"git+https://github.com/facebookincubator/gloo.git#commit=${_gloo_commit}"
        'thirdparty-googletest-git'::"git+https://github.com/google/googletest.git#commit=${_googletest_commit}"
        'thirdparty-ios-cmake-git'::"git+https://github.com/Yangqing/ios-cmake.git#commit=${_ios_cmake_commit}"
        'thirdparty-nccl-git'::"git+https://github.com/NVIDIA/nccl.git#commit=${_nccl_commit}"
        'thirdparty-nervanagpu-git'::"git+https://github.com/NervanaSystems/nervanagpu.git#commit=${_nervanagpu_commit}"
        'thirdparty-NNPACK-git'::"git+https://github.com/Maratyszcza/NNPACK.git#commit=${_nnpack_commit}"
        "thirdparty-protobuf-${_protobuf_version}.tar.gz"::"https://github.com/google/protobuf/archive/v${_protobuf_version}.tar.gz"
        'thirdparty-pybind11-git'::"git+https://github.com/pybind/pybind11.git#commit=${_pybind11_commit}"
        'thirdparty-NNPACK_deps-FP16-git'::"git+https://github.com/Maratyszcza/FP16.git#commit=${_nnpackdeps_fp16_commit}"
        'thirdparty-NNPACK_deps-FXdiv-git'::"git+https://github.com/Maratyszcza/FXdiv.git#commit=${_nnpackdeps_fxdiv_commit}"
        'thirdparty-NNPACK_deps-psimd-git'::"git+https://github.com/Maratyszcza/psimd.git#commit=${_nnpackdeps_psimd_commit}"
        'thirdparty-NNPACK_deps-pthreadpool-git'::"git+https://github.com/Maratyszcza/pthreadpool.git#commit=${_nnpackdeps_pthreadpool_commit}"
)
noextract=("thirdparty-eigen-${_eigen_version}.tar.gz"
           "thirdparty-protobuf-${_protobuf_version}.tar.gz")
sha256sums=('b8f266ed283efc172fa96c06c878ed7f125755f89cde480580b754c1f03c0bab'
            '1c94a1ecc0fe2a52c50c9d1a7bfca655d60c08d48995b27c73aa22b6c375da54'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '78fe37183e04aa8ca2d938df57b93f9489448d38c10fb470cf51c332a461f371'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '0a0ae63cbffc274efb573bdde9a253e3f32e458c41261df51c5dbc5ad541e8f7'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
)

prepare() {
    cd "${pkgname}-${pkgver}/third_party"
    
    local _thirdparty_nongit_list="eigen protobuf"
    local _thirdparty_git_list="android-cmake benchmark cnmem cub gloo googletest \
                                ios-cmake nccl nervanagpu NNPACK pybind11"
    local _nnpackdeps_list="FP16 FXdiv psimd pthreadpool"
    
    for _component in $_thirdparty_nongit_list
    do
        cd "$_component"
        bsdtar -xf "${srcdir}/thirdparty-${_component}"* -s'|[^/]*/||'
        cd ..
    done
    
    for _component in $_thirdparty_git_list
    do
        rm -rf "$_component"
        ln -sf "${srcdir}/thirdparty-${_component}-git" "${_component}"
    done
    
    cd NNPACK_deps
    for _component in $_nnpackdeps_list
    do
        rm -rf "$_component"
        ln -sf "${srcdir}/thirdparty-NNPACK_deps-${_component}-git" "${_component}"
    done
    
    unset _component
    
    # avoid compile errors with nnpack if system library is found
    # https://github.com/caffe2/caffe2/pull/808
    cd "${srcdir}/${pkgname}-${pkgver}"
    patch -Np1 -i "${srcdir}/external-nnpack-fix.patch"
}

build() {
    cd "${pkgname}-${pkgver}"
    mkdir -p build
    cd build
    
    cmake \
        -DBLAS:STRING='Eigen' \
        \
        -DBUILD_BINARY:BOOL='ON' \
        -DBUILD_PYTHON:BOOL='ON' \
        -DBUILD_SHARED_LIBS:BOOL='ON' \
        \
        -DBUILD_TEST:BOOL='OFF' \
        \
        -DCAFFE2_CPU_FLAGS:BOOL='OFF' \
        -DCMAKE_BUILD_TYPE:STRING='Release' \
        -DCMAKE_COLOR_MAKEFILE:BOOL='ON' \
        -DCMAKE_CXX_COMPILER='/usr/bin/g++-5' \
        -DCMAKE_CXX_FLAGS:STRING="$(printf '%s' "$CXXFLAGS" | sed 's/-fno-plt//')" \
        -DCMAKE_C_COMPILER='/usr/bin/gcc-5' \
        -DCMAKE_C_FLAGS:STRING="$(printf '%s' "$CFLAGS" | sed 's/-fno-plt//')" \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL='NO' \
        -DCMAKE_SKIP_RPATH:BOOL='NO' \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL='FALSE' \
        \
        -DCUDA_64_BIT_DEVICE_CODE:BOOL='ON' \
        -DCUDA_ARCH_NAME:STRING='Auto' \
        -DCUDA_ATTACH_VS_BUILD_RULE_TO_CUDA_FILE:BOOL='ON' \
        -DCUDA_BUILD_CUBIN:BOOL='OFF' \
        -DCUDA_BUILD_EMULATION:BOOL='OFF' \
        -DCUDA_HOST_COMPILATION_CPP:BOOL='ON' \
        -DCUDA_HOST_COMPILER:FILEPATH='/usr/bin/gcc-5' \
        -DCUDA_NVCC_EXECUTABLE:FILEPATH='/opt/cuda/bin/nvcc' \
        -DCUDA_PROPAGATE_HOST_FLAGS:BOOL='ON' \
        -DCUDA_SDK_ROOT_DIR:PATH='/opt/cuda' \
        -DCUDA_SEPARABLE_COMPILATION:BOOL='OFF' \
        -DCUDA_TOOLKIT_INCLUDE:PATH='/opt/cuda/include' \
        -DCUDA_TOOLKIT_ROOT_DIR:PATH='/opt/cuda' \
        -DCUDA_USE_STATIC_CUDA_RUNTIME:BOOL='OFF' \
        -DCUDA_VERBOSE_BUILD:BOOL='OFF' \
        -DCUDA_VERSION:STRING='8.0' \
        -DCUDNN_INCLUDE_DIR:PATH='/opt/cuda/include' \
        -DCUDNN_ROOT_DIR:PATH='/opt/cuda' \
        \
        -DGLOO_STATIC_OR_SHARED:STRING='STATIC' \
        -DNCCL_INCLUDE_DIR:PATH='/opt/cuda/include' \
        -DNCCL_LIBRARY:FILEPATH='/opt/cuda/lib64/libnccl.so' \
        -DNCCL_ROOT_DIR:PATH='/opt/cuda' \
        \
        -DOpenCV_DIR:PATH='/usr/share/OpenCV' \
        \
        -DPYTHON_EXECUTABLE:FILEPATH='/usr/bin/python2.7' \
        -DPYTHON_INCLUDE_DIR:PATH='/usr/include/python2.7' \
        -DPYTHON_LIBRARY:FILEPATH='/usr/lib/libpython2.7.so' \
        \
        -DUSE_CNMEM:BOOL='OFF' \
        -DUSE_CUDA:BOOL='ON' \
        -DUSE_GFLAGS:BOOL='ON' \
        -DUSE_GLOG:BOOL='ON' \
        -DUSE_GLOO:BOOL='ON' \
        -DUSE_LEVELDB:BOOL='ON' \
        -DUSE_LITE_PROTO:BOOL='OFF' \
        -DUSE_LMDB:BOOL='ON' \
        -DUSE_MPI:BOOL='ON' \
        -DUSE_NCCL:BOOL='ON' \
        -DUSE_NERVANA_GPU:BOOL='ON' \
        -DUSE_NNPACK:BOOL='ON' \
        -DUSE_OPENCV:BOOL='OFF' \
        -DUSE_OPENMP:BOOL='ON' \
        -DUSE_REDIS:BOOL='ON' \
        -DUSE_ROCKSDB:BOOL='OFF' \
        -DUSE_THREADS:BOOL='ON' \
        -DUSE_ZMQ:BOOL='ON' \
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
    install -D -m644 'LICENSE' "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 'PATENTS' "${pkgdir}/usr/share/licenses/${pkgname}/PATENTS"
}

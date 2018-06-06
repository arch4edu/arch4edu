# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

# NOTE:
# In order to build with NCCL support, follow these steps:
#   1) uncomment the nccl line in 'depends'
#   2) in 'build()', change '-DUSE_NCCL:BOOL=OFF' from 'OFF' to 'ON'
#   3) add these options to cmake command line:
#       -DNCCL_INCLUDE_DIR:PATH='/opt/cuda/include'
#       -DNCCL_ROOT_DIR:PATH='/opt/cuda'

# third_party with no stable release at the target commit
_aten_cpuinfo_commit='d0222b47948234cc01983243a2e0ede018f97f3a'
_nanopb_commit='14efb1a47a496652ab08b1ebcefb0ea24ae4a5e4'
_pybind11_commit='add56ccdcac23a6c522a2c1174a866e293c61dab'
_cub_commit='285aeebaa34b0e8a7670867a2e66c1a52d998d6a'
_eigen_commit='5a0ab9ff4e258b860470afe36e83a3e88b3ce14c'
_googletest_commit='69e48e92de43960a316a826293510b7b3deb9eca'
_nervanagpu_commit='d4eefd50fbd7d34a17dddbc829888835d67b5f4a'
_benchmark_commit='491360b833aaab96818dce256a8409f6296dd995'
_ios_cmake_commit='8abaed637d56f1337d6e1d2c4026e25c1eade724'
_nnpack_commit='b63fe1ba8963f1756b8decc593766615cee99c35'
_gloo_commit='aad0002fb40612e991390d8e807f247ed23f13c5'
_nnpdeps_pthreadp_commit='2b06b31f6a315162348e1f3c24325eedaf6cc559'
_nnpdeps_fxdiv_commit='811b482bcd9e8d98ad80c6c78d5302bb830184b0'
_nnpdeps_fp16_commit='43d6d17df48ebf622587e7ed9472ea76573799b9'
_nnpdeps_psimd_commit='4ac61b112252778b174575931c641bef661ab3cd'
_zstd_commit='aec56a52fbab207fc639a1937d1e708a282edca8'
_cpuinfo_commit='831dc28341b5f20d13e840caf87eaba644d82643'
_python_enum_commit='4cfedc426c4e2fc52e3f5c2b4297e15ed8d6b8c7'
_python_peachpy_commit='07d8fde8ac45d7705129475c0f94ed8925b93473'
_computelibrary_commit='292227986edb37b01061afcad6df18ba9d6ccbeb'
_onnx_commit='7e1bed51cc508a25b22130de459830b5d5063c41'

# third_party with stable release at the target commit
_aten_tbb_version='2018_U2'  # commit '4c73c3b5d7f78c40f69e0c04fd4afb9f48add1e6' is version '2018_U2'
_aten_catch_version='2.2.1'  # commit '0a34cc201ef28bf25c88b0062f331369596cb7b7' is version '2.2.1'
_protobuf_version='3.5.0'    # commit '2761122b810fe8861004ae785cc3ab39f384d342' is version '3.5.0'
_python_six_version='1.11.0' # commit '15e31431af97e5e64b80af0a3f598d382bcdd49a' is version '1.11.0'

_ptver=0.4.0 # pytorch stable release version

pkgname=caffe2
pkgver="0.8.2.pytorch.${_ptver}"
pkgrel=4
pkgdesc='A new lightweight, modular, and scalable deep learning framework (gpu enabled)'
arch=('x86_64')
url='http://caffe2.ai/'
license=('BSD')
depends=(
    # official repositories:
        # required:
            'google-glog' 'protobuf' 'lapack' 'python' 'python-numpy' 'python-protobuf'
            'cuda' 'cudnn'
        # not required but enabled in build:
            'gflags' 'gtest' 'openmp' 'leveldb' 'lmdb' 'numactl' 'openmpi' 'snappy'
            'zeromq' 'hiredis' 'ffmpeg'
        # python:
            'python-flask' 'python-future' 'graphviz' 'python-hypothesis'
            'python-jupyter_core' 'python-matplotlib' 'python-pydot' 'python-yaml'
            'python-requests' 'python-scipy' 'python-setuptools' 'python-six'
            'python-tornado' 'python-gflags' 'python-pyzmq'
    # AUR:
        # not required and disabled in build:
            #'nccl'
        # python:
            'python-nvd3' 'python-scikit-image' 'python-glog' 'python-leveldb'
            'python-lmdb'
)
makedepends=('git' 'cmake' 'gcc54')
conflicts=('caffe' 'caffe-cpu' 'caffe-git' 'caffe-cpu-git'
           'caffe2-git' 'caffe2-cpu' 'caffe2-cpu-git')
options=('!emptydirs')
source=(
    # main source:
        "pytorch-${_ptver}.tar.gz"::"https://github.com/pytorch/pytorch/archive/v${_ptver}.tar.gz"
    # third party:
        'caffe2-thirdparty-aten-cpuinfo-git'::"git+https://github.com/Maratyszcza/cpuinfo#commit=${_aten_cpuinfo_commit}"
        "caffe2-thirdparty-aten-tbb-${_aten_tbb_version}.tar.gz"::"https://github.com/01org/tbb/archive/${_aten_tbb_version}.tar.gz"
        "caffe2-thirdparty-aten-catch-${_aten_catch_version}.tar.gz"::"https://github.com/catchorg/Catch2/archive/v${_aten_catch_version}.tar.gz"
        'caffe2-thirdparty-nanopb-git'::"git+https://github.com/nanopb/nanopb.git#commit=${_nanopb_commit}"
        'caffe2-thirdparty-pybind11-git'::"git+https://github.com/pybind/pybind11.git#commit=${_pybind11_commit}"
        'caffe2-thirdparty-cub-git'::"git+https://github.com/NVlabs/cub.git#commit=${_cub_commit}"
        'caffe2-thirdparty-eigen-git'::"git+https://github.com/eigenteam/eigen-git-mirror.git#commit=${_eigen_commit}"
        'caffe2-thirdparty-googletest-git'::"git+https://github.com/google/googletest.git#commit=${_googletest_commit}"
        'caffe2-thirdparty-nervanagpu-git'::"git+https://github.com/NervanaSystems/nervanagpu.git#commit=${_nervanagpu_commit}"
        'caffe2-thirdparty-benchmark-git'::"git+https://github.com/google/benchmark.git#commit=${_benchmark_commit}"
        "caffe2-thirdparty-protobuf-${_protobuf_version}.tar.gz"::"https://github.com/google/protobuf/archive/v${_protobuf_version}.tar.gz"
        'caffe2-thirdparty-ios-cmake-git'::"git+https://github.com/Yangqing/ios-cmake.git#commit=${_ios_cmake_commit}"
        'caffe2-thirdparty-NNPACK-git'::"git+https://github.com/Maratyszcza/NNPACK.git#commit=${_nnpack_commit}"
        'caffe2-thirdparty-gloo-git'::"git+https://github.com/facebookincubator/gloo.git#commit=${_gloo_commit}"
        'caffe2-thirdparty-NNPACK_deps-pthreadpool-git'::"git+https://github.com/Maratyszcza/pthreadpool.git#commit=${_nnpdeps_pthreadp_commit}"
        'caffe2-thirdparty-NNPACK_deps-FXdiv-git'::"git+https://github.com/Maratyszcza/FXdiv.git#commit=${_nnpdeps_fxdiv_commit}"
        'caffe2-thirdparty-NNPACK_deps-FP16-git'::"git+https://github.com/Maratyszcza/FP16.git#commit=${_nnpdeps_fp16_commit}"
        'caffe2-thirdparty-NNPACK_deps-psimd-git'::"git+https://github.com/Maratyszcza/psimd.git#commit=${_nnpdeps_psimd_commit}"
        'caffe2-thirdparty-zstd-git'::"git+https://github.com/facebook/zstd.git#commit=${_zstd_commit}"
        'caffe2-thirdparty-cpuinfo-git'::"git+https://github.com/Maratyszcza/cpuinfo.git#commit=${_cpuinfo_commit}"
        'caffe2-thirdparty-python-enum-git'::"git+https://github.com/PeachPy/enum34.git#commit=${_python_enum_commit}"
        'caffe2-thirdparty-python-peachpy-git'::"git+https://github.com/Maratyszcza/PeachPy.git#commit=${_python_peachpy_commit}"
        "caffe2-thirdparty-python-six-${_python_six_version}.tar.gz"::"https://github.com/benjaminp/six/archive/${_python_six_version}.tar.gz"
        'caffe2-thirdparty-ComputeLibrary-git'::"git+https://github.com/ARM-software/ComputeLibrary.git#commit=${_computelibrary_commit}"
        'caffe2-thirdparty-onnx-git'::"git+https://github.com/onnx/onnx.git#commit=${_onnx_commit}"
)
noextract=("caffe2-thirdparty-aten-tbb-${_aten_tbb_version}.tar.gz"
           "caffe2-thirdparty-aten-catch-${_aten_catch_version}.tar.gz"
           "thirdparty-protobuf-${_protobuf_version}.tar.gz"
           "caffe2-thirdparty-python-six-${_python_six_version}.tar.gz"
)
sha256sums=('f91c059710f802c91bed8207f2d461851b1bc2d44f7cd6e9aaa548392db9412f'
            'SKIP'
            '78bb9bae474736d213342f01fe1a6d00c6939d5c75b367e2e43e7bf29a6d8eca'
            '3938bc896f8de570bc56d25606fc128437ee53590a95cf3e005710176a1a1ce4'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '0cc6607e2daa675101e9b7398a436f09167dffb8ca0489b0307ff7260498c13c'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            '927dc6fcfccd4e32e1ce161a20bf8cda39d8c9d5f7a845774486907178f69bd4'
            'SKIP'
            'SKIP')

prepare() {
    local _thirdparty_git_list="nanopb pybind11 cub eigen googletest nervanagpu \
                                benchmark ios-cmake NNPACK gloo zstd cpuinfo \
                                python-enum python-peachpy ComputeLibrary onnx"
                                
    local _nnpackdeps_list='pthreadpool FXdiv FP16 psimd'
    
    cd "pytorch-${_ptver}/aten/src/ATen/cpu"
    rm -rf cpuinfo
    ln -sf "${srcdir}/caffe2-thirdparty-aten-cpuinfo-git" cpuinfo
    
    cd "${srcdir}/pytorch-${_ptver}/aten/src/ATen/cpu/tbb/tbb_remote"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-aten-tbb-${_aten_tbb_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_ptver}/aten/src/ATen/utils/catch"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-aten-catch-${_aten_catch_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_ptver}/third_party/protobuf"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-protobuf-${_protobuf_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_ptver}/third_party/python-six"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-python-six-${_python_six_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_ptver}/third_party"
    
    for _component in $_thirdparty_git_list
    do
        rm -rf "$_component"
        ln -sf "${srcdir}/caffe2-thirdparty-${_component}-git" "${_component}"
    done
    
    for _component in $_nnpackdeps_list
    do
        rm -rf "$_component"
        ln -sf "${srcdir}/caffe2-thirdparty-NNPACK_deps-${_component}-git" "${_component}"
    done
    
    # fix build if eigen is installed (use eigen from third_party folder)
    cd "${srcdir}/pytorch-${_ptver}"
    local _eigen='  message(STATUS "Using Eigen third party subdirectory for compatibility.")'
    sed -i '/find_package(Eigen3)/s/^/#/' cmake/Dependencies.cmake
    sed -i "/Did[[:space:]]not[[:space:]]find[[:space:]]system[[:space:]]Eigen/s/.*/${_eigen}/" cmake/Dependencies.cmake
}

build() {
    cd "pytorch-${_ptver}"
    
    local _pythonver="$(python --version | sed 's/^Python[[:space:]]//' | grep -o '^[0-9]*\.[0-9]*')"
    
    mkdir -p build
    cd build
    
    cmake \
        -DBLAS:STRING='Eigen' \
        \
        -DBUILD_BINARY:BOOL='ON' \
        -DBUILD_DOCS:BOOL='OFF' \
        -DBUILD_PYTHON:BOOL='ON' \
        -DBUILD_SHARED_LIBS:BOOL='ON' \
        \
        -DBUILD_TEST:BOOL='OFF' \
        \
        -DCMAKE_COLOR_MAKEFILE:BOOL='ON' \
        -DCMAKE_CXX_COMPILER='/usr/bin/g++-5' \
        -DCMAKE_CXX_FLAGS:STRING="${CXXFLAGS/-fno-plt/}" \
        -DCMAKE_C_COMPILER='/usr/bin/gcc-5' \
        -DCMAKE_C_FLAGS:STRING="${CFLAGS/-fno-plt/}" \
        -DCMAKE_INSTALL_LIBDIR:PATH='lib' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL='NO' \
        -DCMAKE_SKIP_RPATH:BOOL='NO' \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL='FALSE' \
        \
        -DCUDA_ARCH_NAME:STRING='Auto' \
        -DCUDA_64_BIT_DEVICE_CODE:BOOL='ON' \
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
        -DCUDNN_INCLUDE_DIR:PATH='/opt/cuda/include' \
        -DCUDNN_LIBRARY:FILEPATH='/opt/cuda/lib64/libcudnn.so' \
        -DCUDNN_ROOT_DIR:PATH='/opt/cuda' \
        \
        -DGLOO_STATIC_OR_SHARED:STRING='STATIC' \
        \
        -DOpenCV_DIR:PATH='/usr/share/OpenCV' \
        \
        -DPYTHON_EXECUTABLE:FILEPATH="/usr/bin/python${_pythonver}" \
        -DPYTHON_INCLUDE_DIR:PATH="/usr/include/python${_pythonver}m" \
        -DPYTHON_LIBRARY:FILEPATH="/usr/lib/libpython${_pythonver}m.so" \
        \
        -DUSE_ACL:BOOL='OFF' \
        -DUSE_ASAN:BOOL='OFF' \
        -DUSE_ATEN:BOOL='OFF' \
        -DUSE_CUDA:BOOL='ON' \
        -DUSE_FFMPEG:BOOL='ON' \
        -DUSE_GFLAGS:BOOL='ON' \
        -DUSE_GLOG:BOOL='ON' \
        -DUSE_GLOO:BOOL='ON' \
        -DUSE_LEVELDB:BOOL='ON' \
        -DUSE_LITE_PROTO:BOOL='OFF' \
        -DUSE_LMDB:BOOL='ON' \
        -DUSE_METAL:BOOL='OFF' \
        -DUSE_MOBILE_OPENGL:BOOL='OFF' \
        -DUSE_MPI:BOOL='ON' \
        -DUSE_NCCL:BOOL='OFF' \
        -DUSE_NERVANA_GPU:BOOL='OFF' \
        -DUSE_NNAPI:BOOL='OFF' \
        -DUSE_NNPACK:BOOL='ON' \
        -DUSE_NUMA:BOOL='ON' \
        -DUSE_OBSERVERS:BOOL='ON' \
        -DUSE_OPENCV:BOOL='OFF' \
        -DUSE_OPENMP:BOOL='ON' \
        -DUSE_PROF:BOOL='OFF' \
        -DUSE_REDIS:BOOL='ON' \
        -DUSE_ROCKSDB:BOOL='OFF' \
        -DUSE_SNPE:BOOL='OFF' \
        -DUSE_TENSORRT:BOOL='OFF' \
        -DUSE_ZMQ:BOOL='ON' \
        -DUSE_ZSTD:BOOL='ON' \
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
    cd "pytorch-${_ptver}/build"
    
    make DESTDIR="$pkgdir" install
    
    # remove unneeded files
    rm -rf "${pkgdir}/usr/include/google"
    rm -rf "${pkgdir}/usr/lib/cmake/protobuf"
    rm -f "$pkgdir"/usr/bin/{protoc,unzstd,zstd{cat,mt,}}
    rm -f "$pkgdir"/usr/include/{{bitcasts,cpuinfo,fp16,fxdiv,nnpack,psimd,pthreadpool,zbuff,zdict,zstd*}.h,{__init__,avx{,2}}.py}
    rm -f "$pkgdir"/usr/lib/lib{{cpuinfo,nnpack,protobuf-lite,protobuf,protoc,pthreadpool,zstd}.a,zstd.so*}
    rm -f "$pkgdir"/usr/lib/pkgconfig/{protobuf-lite,protobuf}.pc
    rm -f "$pkgdir"/usr/share/pkgconfig/libzstd.pc
    rm -f "$pkgdir"/usr/share/man/man1/{unzstd,zstd{cat,}}.1
    
    # license
    cd "${srcdir}/pytorch-${_ptver}"
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 NOTICE  "${pkgdir}/usr/share/licenses/${pkgname}/NOTICE"
}

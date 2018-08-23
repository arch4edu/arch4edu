# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

# third_party with no stable release at the target commit
_nanopb_commit='14efb1a47a496652ab08b1ebcefb0ea24ae4a5e4'
_pybind11_commit='add56ccdcac23a6c522a2c1174a866e293c61dab'
_cub_commit='285aeebaa34b0e8a7670867a2e66c1a52d998d6a'
_eigen_commit='e9e95489a0b241412e31f0525e85b2fab386c786'
_googletest_commit='69e48e92de43960a316a826293510b7b3deb9eca'
_nervanagpu_commit='d4eefd50fbd7d34a17dddbc829888835d67b5f4a'
_benchmark_commit='505be96ab23056580a3a2315abba048f4428b04e'
_ios_cmake_commit='8abaed637d56f1337d6e1d2c4026e25c1eade724'
_nnpack_commit='3eb0d453662d05a708f43b108bed9e17b705383e'
_gloo_commit='69eef748cc1dfbe0fefed69b34e6545495f67ac5'
_nnpdeps_pthreadp_commit='2b06b31f6a315162348e1f3c24325eedaf6cc559'
_nnpdeps_fxdiv_commit='811b482bcd9e8d98ad80c6c78d5302bb830184b0'
_nnpdeps_fp16_commit='43d6d17df48ebf622587e7ed9472ea76573799b9'
_nnpdeps_psimd_commit='4ac61b112252778b174575931c641bef661ab3cd'
_zstd_commit='aec56a52fbab207fc639a1937d1e708a282edca8'
_cpuinfo_commit='1e6c8c99d27f2b5eb9d2e6231055c6a4115b85e5'
_python_enum_commit='4cfedc426c4e2fc52e3f5c2b4297e15ed8d6b8c7'
_python_peachpy_commit='07d8fde8ac45d7705129475c0f94ed8925b93473'
_computelibrary_commit='292227986edb37b01061afcad6df18ba9d6ccbeb'
_onnx_commit='b2817a682f25f960586f06caa539bbbd7a96b859'
_onnx_tensorrt_commit='fa0964e8477fc004ee2f49ee77ffce0bf7f711a9'
_sleef_commit='6ff7a135a1e31979d1e1844a2e7171dfbd34f54f'

# third_party with stable release at the target commit
_catch_version='2.2.1'       # commit '0a34cc201ef28bf25c88b0062f331369596cb7b7' is version '2.2.1'
_protobuf_version='3.5.0'    # commit '2761122b810fe8861004ae785cc3ab39f384d342' is version '3.5.0'
_python_six_version='1.11.0' # commit '15e31431af97e5e64b80af0a3f598d382bcdd49a' is version '1.11.0'
_cereal_version='1.2.2'      # commit '51cbda5f30e56c801c07fe3d3aba5d7fb9e6cca4' is version '1.2.2'
_ideep_version='2.0.0_b1'    # commit '4bd9a6800bf7db068187619e0582d34dec9651dc' is version '2.0.0_b1'

_pytorchver=0.4.1 # pytorch stable release version

pkgname=caffe2
pkgver="0.8.2.pytorch.${_pytorchver}"
pkgrel=2
pkgdesc='A new lightweight, modular, and scalable deep learning framework'
arch=('i686' 'x86_64')
url='http://caffe2.ai/'
license=('BSD')
depends=(
    # official repositories:
        # required:
            'google-glog' 'protobuf' 'lapack' 'python' 'python-numpy' 'python-protobuf'
        # not required but enabled in build:
            'gflags' 'gtest' 'openmp' 'leveldb' 'lmdb' 'numactl' 'openmpi' 'snappy'
            'zeromq' 'hiredis' 'ocl-icd' 'opencv' 'gtk3' 'ffmpeg'
        # python:
            'python-flask' 'python-future' 'graphviz' 'python-hypothesis'
            'python-jupyter_core' 'python-matplotlib' 'python-pydot' 'python-yaml'
            'python-requests' 'python-scipy' 'python-setuptools' 'python-six'
            'python-tornado' 'python-gflags' 'python-pyzmq'
    # AUR:
        # not required but enabled in build:
            'libibverbs'
        # python:
            'python-nvd3' 'python-scikit-image' 'python-glog' 'python-leveldb'
            'python-lmdb'
)
makedepends=('git' 'cmake' 'opencl-headers')
conflicts=('caffe2-git' 'caffe2-cuda' 'caffe2-cuda-git' 'caffe2-cpu' 'caffe2-cpu-git'
           'caffe' 'caffe-git' 'caffe-cuda' 'caffe-cuda-git')
replaces=('caffe2-cpu')
options=('!emptydirs')
source=(
    # main source:
        "pytorch-${_pytorchver}.tar.gz"::"https://github.com/pytorch/pytorch/archive/v${_pytorchver}.tar.gz"
    # third party:
        "caffe2-thirdparty-catch-${_catch_version}.tar.gz"::"https://github.com/catchorg/Catch2/archive/v${_catch_version}.tar.gz"
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
        "caffe2-thirdparty-cereal-${_cereal_version}.tar.gz"::"https://github.com/USCiLab/cereal/archive/v${_cereal_version}.tar.gz"
        'caffe2-thirdparty-onnx-tensorrt-git'::"git+https://github.com/onnx/onnx-tensorrt.git#commit=${_onnx_tensorrt_commit}"
        'caffe2-thirdparty-sleef-git'::"git+https://github.com/shibatch/sleef.git#commit=${_sleef_commit}"
        "caffe2-thirdparty-ideep-${_ideep_version}.tar.gz"::"https://github.com/intel/ideep/archive/v${_ideep_version}.tar.gz"
)
noextract=("caffe2-thirdparty-catch-${_catch_version}.tar.gz"
           "caffe2-thirdparty-protobuf-${_protobuf_version}.tar.gz"
           "caffe2-thirdparty-python-six-${_python_six_version}.tar.gz"
           "caffe2-thirdparty-cereal-${_cereal_version}.tar.gz"
           "caffe2-thirdparty-ideep-${_ideep_version}.tar.gz"
)
sha256sums=('6ab03fa707909e5fb6209a3a98d24c25cd64d9590f3e05d6e8490e4d07b3a765'
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
            'SKIP'
            '1921f26d2e1daf9132da3c432e2fd02093ecaedf846e65d7679ddf868c7289c4'
            'SKIP'
            'SKIP'
            '9fa1e75035273494d12425194140b3a884b2e70552b4bad3a111e861881876b5')

prepare() {
    local _thirdparty_git_list="nanopb pybind11 cub eigen googletest nervanagpu \
                                benchmark ios-cmake NNPACK gloo zstd cpuinfo \
                                python-enum python-peachpy ComputeLibrary onnx \
                                onnx-tensorrt sleef"
                                
    local _nnpackdeps_list='pthreadpool FXdiv FP16 psimd'
    
    local _component
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party/catch"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-catch-${_catch_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party/protobuf"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-protobuf-${_protobuf_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party/python-six"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-python-six-${_python_six_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party/cereal"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-cereal-${_cereal_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party/ideep"
    bsdtar -xf "${srcdir}/caffe2-thirdparty-ideep-${_ideep_version}.tar.gz" -s'|[^/]*/||'
    
    cd "${srcdir}/pytorch-${_pytorchver}/third_party"
    
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
}

build() {
    cd "pytorch-${_pytorchver}"
    
    local _pythonver
    _pythonver="$(python --version | awk '{ print $2 }' | grep -o '^[0-9]*\.[0-9]*')"
    
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
        -DCMAKE_INSTALL_LIBDIR:PATH='lib' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL='NO' \
        -DCMAKE_SKIP_RPATH:BOOL='NO' \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL='FALSE' \
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
        -DUSE_ASAN:BOOL='ON' \
        -DUSE_ATEN:BOOL='OFF' \
        -DUSE_CUDA:BOOL='OFF' \
        -DUSE_CUDNN:BOOL='OFF' \
        -DUSE_DISTRIBUTED:BOOL='OFF' \
        -DUSE_DISTRIBUTED_MW:BOOL='OFF' \
        -DUSE_FFMPEG:BOOL='ON' \
        -DUSE_GFLAGS:BOOL='ON' \
        -DUSE_GLOG:BOOL='ON' \
        -DUSE_GLOO:BOOL='ON' \
        -DUSE_GLOO_IBVERBS:BOOL='ON' \
        -DUSE_IBVERBS:BOOL='ON' \
        -DUSE_IDEEP:BOOL='ON' \
        -DUSE_LEVELDB:BOOL='ON' \
        -DUSE_LITE_PROTO:BOOL='OFF' \
        -DUSE_LMDB:BOOL='ON' \
        -DUSE_METAL:BOOL='OFF' \
        -DUSE_MKLDNN:BOOL='OFF' \
        -DUSE_MKLML:BOOL='OFF' \
        -DUSE_MOBILE_OPENGL:BOOL='OFF' \
        -DUSE_MPI:BOOL='ON' \
        -DUSE_NCCL:BOOL='OFF' \
        -DUSE_NERVANA_GPU:BOOL='OFF' \
        -DUSE_NNAPI:BOOL='OFF' \
        -DUSE_NNPACK:BOOL='ON' \
        -DUSE_NUMA:BOOL='ON' \
        -DUSE_NVRTC:BOOL='OFF' \
        -DUSE_OBSERVERS:BOOL='ON' \
        -DUSE_OPENCL:BOOL='ON' \
        -DUSE_OPENCV:BOOL='ON' \
        -DUSE_OPENMP:BOOL='ON' \
        -DUSE_PROF:BOOL='OFF' \
        -DUSE_REDIS:BOOL='ON' \
        -DUSE_ROCKSDB:BOOL='OFF' \
        -DUSE_ROCM:BOOL='OFF' \
        -DUSE_SNPE:BOOL='OFF' \
        -DUSE_SYSTEM_NCCL:BOOL='OFF' \
        -DUSE_TENSORRT:BOOL='OFF' \
        -DUSE_ZMQ:BOOL='ON' \
        -DUSE_ZSTD:BOOL='ON' \
        \
        -Wno-dev \
        ..
        
    make
}

package() {
    cd "pytorch-${_pytorchver}/build"
    
    make DESTDIR="$pkgdir" install
    
    # remove unneeded files
    local _entry
    local _exclude_dirs
    local _exclude_lib
    _exclude_dirs=($(find "${pkgdir}/usr/include" -mindepth 1 -maxdepth 1 -type d ! -name 'caffe*'))
    _exclude_libs=($(find -L "${pkgdir}/usr/lib" -maxdepth 1 -type f ! -name 'libcaffe*'))
    rm -f  "$pkgdir"/usr/bin/{protoc,unzstd,zstd{cat,mt,}}
    rm -f  "$pkgdir"/usr/include/{*.h,*.py}
    rm -rf "$pkgdir"/usr/lib/cmake/protobuf
    rm -f  "$pkgdir"/usr/lib/pkgconfig/{protobuf-lite,protobuf}.pc
    rm -rf "$pkgdir"/usr/share/pkgconfig
    rm -rf "$pkgdir"/usr/share/{ATen,cmake/ATen}
    rm -f  "$pkgdir"/usr/share/man/man1/{unzstd,zstd{cat,}}.1
    for _entry in ${_exclude_dirs[@]} ${_exclude_libs[@]}
    do
        rm -rf "$_entry"
    done
    
    # license
    cd "${srcdir}/pytorch-${_pytorchver}"
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 NOTICE  -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

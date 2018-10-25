# Maintainer : Daniel Bermond < gmail-com: danielbermond >

_catch_commit='0a34cc201ef28bf25c88b0062f331369596cb7b7'
_pybind11_commit='5c8746ff135abb390bf95944be593e895a586a50'
_cub_commit='285aeebaa34b0e8a7670867a2e66c1a52d998d6a'
_eigen_commit='cafae68f33f7f41270b2e8c2dd181f510aa4d918'
_googletest_commit='2fe3bd994b3189899d93f1d5a881e725e046fdc2'
_nervanagpu_commit='d4eefd50fbd7d34a17dddbc829888835d67b5f4a'
_benchmark_commit='505be96ab23056580a3a2315abba048f4428b04e'
_protobuf_commit='2761122b810fe8861004ae785cc3ab39f384d342'
_ios_cmake_commit='8abaed637d56f1337d6e1d2c4026e25c1eade724'
_nnpack_commit='af40ea7d12702f8ae55aeb13701c09cad09334c3'
_gloo_commit='aa0d2e3f8aa4f9cee5ffa46070491cf1ed6aae70'
_nnpdeps_pthreadp_commit='2b06b31f6a315162348e1f3c24325eedaf6cc559'
_nnpdeps_fxdiv_commit='811b482bcd9e8d98ad80c6c78d5302bb830184b0'
_nnpdeps_fp16_commit='43d6d17df48ebf622587e7ed9472ea76573799b9'
_nnpdeps_psimd_commit='4ac61b112252778b174575931c641bef661ab3cd'
_zstd_commit='aec56a52fbab207fc639a1937d1e708a282edca8'
_cpuinfo_commit='4e8f04355892c5deb64a51731a6afdb544a4294d'
_python_enum_commit='4cfedc426c4e2fc52e3f5c2b4297e15ed8d6b8c7'
_python_peachpy_commit='07d8fde8ac45d7705129475c0f94ed8925b93473'
_python_six_commit='15e31431af97e5e64b80af0a3f598d382bcdd49a'
_computelibrary_commit='292227986edb37b01061afcad6df18ba9d6ccbeb'
_onnx_commit='c4734c6200cb42c1aa36eb1f0160041d2401644d'
_cereal_commit='51cbda5f30e56c801c07fe3d3aba5d7fb9e6cca4'
_onnx_tensorrt_commit='fa0964e8477fc004ee2f49ee77ffce0bf7f711a9'
_sleef_commit='6ff7a135a1e31979d1e1844a2e7171dfbd34f54f'
_ideep_commit='dedff8fb8193fe3a1ea893d4bc852f8ea395b6b3'

_pytorchver=1.0rc1 # pytorch stable release version

pkgname=caffe2
pkgver="0.8.2.pytorch.${_pytorchver}"
pkgrel=3
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
            'zeromq' 'hiredis' 'opencv' 'gtk3' 'ffmpeg'
        # python:
            'python-flask' 'python-future' 'graphviz' 'python-hypothesis'
            'python-jupyter_core' 'python-matplotlib' 'python-pydot' 'python-yaml'
            'python-requests' 'python-scipy' 'python-setuptools' 'python-six'
            'python-tornado' 'python-gflags' 'python-pyzmq'
    # AUR:
        # not required but enabled in build:
            'rdma-core'
        # python:
            'python-nvd3' 'python-scikit-image' 'python-glog' 'python-leveldb'
            'python-lmdb'
)
makedepends=('git' 'cmake')
provides=('caffe2-cpu')
conflicts=('caffe2-cpu')
replaces=('caffe2-cpu')
options=('!emptydirs')
source=(
    # main source:
        "pytorch-${_pytorchver}.tar.gz"::"https://github.com/pytorch/pytorch/archive/v${_pytorchver}.tar.gz"
    # third party:
        'caffe2-thirdparty-catch-git'::"git+https://github.com/catchorg/Catch2.git#commit=${_catch_commit}"
        'caffe2-thirdparty-pybind11-git'::"git+https://github.com/pybind/pybind11.git#commit=${_pybind11_commit}"
        'caffe2-thirdparty-cub-git'::"git+https://github.com/NVlabs/cub.git#commit=${_cub_commit}"
        'caffe2-thirdparty-eigen-git'::"git+https://github.com/eigenteam/eigen-git-mirror.git#commit=${_eigen_commit}"
        'caffe2-thirdparty-googletest-git'::"git+https://github.com/google/googletest.git#commit=${_googletest_commit}"
        'caffe2-thirdparty-nervanagpu-git'::"git+https://github.com/NervanaSystems/nervanagpu.git#commit=${_nervanagpu_commit}"
        'caffe2-thirdparty-benchmark-git'::"git+https://github.com/google/benchmark.git#commit=${_benchmark_commit}"
        'caffe2-thirdparty-protobuf-git'::"git+https://github.com/google/protobuf.git#commit=${_protobuf_commit}"
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
        'caffe2-thirdparty-python-six-git'::"git+https://github.com/benjaminp/six.git#commit=${_python_six_commit}"
        'caffe2-thirdparty-ComputeLibrary-git'::"git+https://github.com/ARM-software/ComputeLibrary.git#commit=${_computelibrary_commit}"
        'caffe2-thirdparty-onnx-git'::"git+https://github.com/onnx/onnx.git#commit=${_onnx_commit}"
        'caffe2-thirdparty-cereal-git'::"git+https://github.com/USCiLab/cereal.git#commit=${_cereal_commit}"
        'caffe2-thirdparty-onnx-tensorrt-git'::"git+https://github.com/onnx/onnx-tensorrt.git#commit=${_onnx_tensorrt_commit}"
        'caffe2-thirdparty-sleef-git'::"git+https://github.com/shibatch/sleef.git#commit=${_sleef_commit}"
        'caffe2-thirdparty-ideep-git'::"git+https://github.com/intel/ideep.git#commit=${_ideep_commit}"
)
sha256sums=('473cd4af032ddec4279cf3a90dd9508b6fa0be5cd89c842945f88b5a576a4231'
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
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    cd "${srcdir}/pytorch-${_pytorchver}/third_party"
    
    local _thirdparty_list="catch pybind11 cub eigen googletest nervanagpu \
                            benchmark protobuf ios-cmake NNPACK gloo zstd \
                            cpuinfo python-enum python-peachpy python-six \
                            ComputeLibrary onnx cereal onnx-tensorrt sleef \
                            ideep"
                                
    local _nnpackdeps_list='pthreadpool FXdiv FP16 psimd'
    
    local _component
    
    for _component in $_thirdparty_list
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
        -DUSE_CUDA:BOOL='OFF' \
        -DUSE_CUDNN:BOOL='OFF' \
        -DUSE_DISTRIBUTED:BOOL='ON' \
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
        -DUSE_OPENCL:BOOL='OFF' \
        -DUSE_OPENCV:BOOL='ON' \
        -DUSE_OPENMP:BOOL='ON' \
        -DUSE_PROF:BOOL='OFF' \
        -DUSE_REDIS:BOOL='ON' \
        -DUSE_ROCKSDB:BOOL='OFF' \
        -DUSE_ROCM:BOOL='OFF' \
        -DUSE_SNPE:BOOL='OFF' \
        -DUSE_SYSTEM_EIGEN_INSTALL:BOOL='OFF' \
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
    local _exclude_libs
    _exclude_dirs=($(find "${pkgdir}/usr/include" -mindepth 1 -maxdepth 1 -type d ! -name 'caffe*'))
    _exclude_libs=($(find -L "${pkgdir}/usr/lib" -maxdepth 1 -type f ! -name 'libcaffe*'))
    rm -f  "$pkgdir"/usr/bin/{protoc,unzstd,zstd{cat,mt,}}
    rm -f  "$pkgdir"/usr/include/{*.h,*.py}
    rm -rf "$pkgdir"/usr/lib/cmake/protobuf
    rm -f  "$pkgdir"/usr/lib/pkgconfig/{protobuf-lite,protobuf}.pc
    rm -rf "$pkgdir"/usr/share/pkgconfig
    rm -rf "$pkgdir"/usr/share/{ATen,cmake/{ATen,ONNX}}
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

# Maintainer : Daniel Bermond <dbermond@archlinux.org>

pkgbase=caffe2
pkgname=('caffe2' 'caffe2-cuda')
_pytorchver=1.1.0 # pytorch stable release version
pkgver="0.8.2_${_pytorchver}"
pkgrel=3
pkgdesc='A new lightweight, modular, and scalable deep learning framework'
arch=('x86_64')
url='https://caffe2.ai/'
license=('BSD')
depends=('google-glog' 'protobuf' 'python' 'python-numpy' 'python-protobuf'
         'python-yaml' 'blas' 'lapack' 'gflags')
optdepends=('python-flask' 'graphviz' 'python-hypothesis' 'python-matplotlib'
            'python-pydot' 'python-nvd3' 'python-yaml' 'python-requests'
            'python-scikit-image' 'python-scipy' 'python-setuptools'
            'python-future' 'python-tornado' 'python-six' 'python-lmdb')
makedepends=('git' 'cmake' 'gtest' 'snappy' 'cuda' 'cudnn' 'nccl')
conflicts=('python-pytorch')
options=('!emptydirs')
source=("git+https://github.com/pytorch/pytorch.git#tag=v${_pytorchver}"
        'git+https://github.com/pybind/pybind11'
        'git+https://github.com/NVlabs/cub'
        'git+https://github.com/eigenteam/eigen-git-mirror'
        'git+https://github.com/google/googletest'
        'git+https://github.com/google/benchmark'
        'git+https://github.com/google/protobuf'
        'git+https://github.com/Yangqing/ios-cmake'
        'git+https://github.com/Maratyszcza/NNPACK'
        'git+https://github.com/facebookincubator/gloo'
        'git+https://github.com/Maratyszcza/pthreadpool'
        'git+https://github.com/Maratyszcza/FXdiv'
        'git+https://github.com/Maratyszcza/FP16'
        'git+https://github.com/Maratyszcza/psimd'
        'git+https://github.com/facebook/zstd'
        'git+https://github.com/Maratyszcza/cpuinfo'
        'git+https://github.com/PeachPy/enum34'
        'git+https://github.com/Maratyszcza/PeachPy'
        'git+https://github.com/benjaminp/six'
        'git+https://github.com/onnx/onnx'
        'git+https://github.com/onnx/onnx-tensorrt'
        'sleef-zdevito'::'git+https://github.com/zdevito/sleef'
        'git+https://github.com/intel/ideep'
        'git+https://github.com/NVIDIA/nccl.git'
        'git+https://github.com/google/gemmlowp'
        'git+https://github.com/pytorch/QNNPACK'
        'git+https://github.com/intel/ARM_NEON_2_x86_SSE'
        'git+https://github.com/pytorch/fbgemm'
        'git+https://github.com/houseroad/foxi')
sha256sums=('SKIP'
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
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
    mkdir -p pytorch/{build-cpu-only,build-cuda}
    
    cd pytorch
    
    # submodules which clone dir coincide with the submodule name
    local _submodule_list=('pybind11'
                           'cub'
                           'googletest'
                           'benchmark'
                           'protobuf'
                           'ios-cmake'
                           'NNPACK'
                           'gloo'
                           'zstd'
                           'onnx'
                           'onnx-tensorrt'
                           'sleef'
                           'ideep'
                           'QNNPACK'
                           'fbgemm'
                           'foxi')
    local _submodule
    for _submodule in "${_submodule_list[@]}"
    do
        git config --local "submodule.third_party/${_submodule}.url" "${srcdir}/${_submodule}"
    done
    
    # submodules which clone dir does not coincide with the submodule name
    git config --local "submodule.third_party/eigen.url" "${srcdir}/eigen-git-mirror"
    git config --local "submodule.third_party/NNPACK_deps/pthreadpool.url" "${srcdir}/pthreadpool"
    git config --local "submodule.third_party/NNPACK_deps/FXdiv.url" "${srcdir}/FXdiv"
    git config --local "submodule.third_party/NNPACK_deps/FP16.url" "${srcdir}/FP16"
    git config --local "submodule.third_party/NNPACK_deps/psimd.url" "${srcdir}/psimd"
    git config --local "submodule.third_party/python-enum.url" "${srcdir}/enum34"
    git config --local "submodule.third_party/python-peachpy.url" "${srcdir}/PeachPy"
    git config --local "submodule.third_party/python-six.url" "${srcdir}/six"
    git config --local "submodule.third_party/sleef.url" "${srcdir}/sleef-zdevito"
    git config --local "submodule.third_party/neon2sse.url" "${srcdir}/ARM_NEON_2_x86_SSE"
    git config --local "submodule.third_party/nccl/nccl.url" "${srcdir}/nccl"
    git config --local "submodule.third_party/gemmlowp/gemmlowp.url" "${srcdir}/gemmlowp"
    
    # special case (upstream uses third-party instead of third_party)
    git config --local 'submodule.third-party/cpuinfo.url' "${srcdir}/cpuinfo"
    
    git submodule update
}

build() {
    local _common_opts=('..'
                        '-DBLAS:STRING=Eigen'
                        '-DBUILD_BINARY:BOOL=ON'
                        '-DBUILD_CUSTOM_PROTOBUF:BOOL=OFF'
                        '-DBUILD_SHARED_LIBS:BOOL=ON'
                        '-DCMAKE_BUILD_TYPE:STRING=None'
                        '-DCMAKE_INSTALL_LIBDIR:PATH=lib'
                        '-DCMAKE_INSTALL_PREFIX:PATH=/usr'
                        '-DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES'
                        '-DCXX_AVX2_FOUND:BOOL=FALSE'
                        '-DCXX_AVX_FOUND:BOOL=FALSE'
                        '-DC_AVX2_FOUND:BOOL=FALSE'
                        '-DC_AVX_FOUND:BOOL=FALSE'
                        '-DUSE_GFLAGS:BOOL=ON'
                        '-DUSE_GLOG:BOOL=ON'
                        '-DUSE_MPI:BOOL=OFF'
                        '-DUSE_NUMA:BOOL=OFF'
                        '-DUSE_OPENCV:BOOL=OFF'
                        '-Wno-dev')
    
    # caffe2-cuda
    cd pytorch/build-cuda
    cmake \
        "${_common_opts[@]}" \
        -DCMAKE_CXX_COMPILER:FILEPATH='/opt/cuda/bin/g++' \
        -DCMAKE_C_COMPILER:FILEPATH='/opt/cuda/bin/gcc' \
        -DCUDA_HOST_COMPILER:FILEPATH='/opt/cuda/bin/gcc' \
        -DCUDA_NVCC_FLAGS:STRING='-Xfatbin -compress-all' \
        -DTORCH_CUDA_ARCH_LIST='3.0;3.2;3.5;3.7;5.0;5.2;5.3;6.0;6.1;6.2;7.0;7.2;7.5' \
        -DUSE_CUDA:BOOL='ON' \
        -DUSE_CUDNN:BOOL='ON' \
        -DUSE_METAL:BOOL='OFF' \
        -DUSE_NCCL:BOOL='ON' \
        -DUSE_SYSTEM_NCCL:BOOL='ON'
    ## fix: avoid a second compilation in package()
    sed -i 's/^preinstall:[[:space:]]all/preinstall:/' Makefile
    make
    
    # caffe2 (cpu only, without cuda support)
    cd "${srcdir}/pytorch/build-cpu-only"
    cmake "${_common_opts[@]}" -DUSE_CUDA:BOOL='OFF' -DUSE_NCCL:BOOL='OFF'
    make
}

_package_common() {
    make DESTDIR="$pkgdir" install
    
    # remove unneeded files
    rm    "$pkgdir"/usr/include/*.h
    rm    "$pkgdir"/usr/lib/{*.a,lib{foxi*,onnxifi*}.so*}
    rm -r "$pkgdir"/usr/share/{ATen,cmake/{ATen,Gloo,ONNX}}
    rm -r "$pkgdir"/torch
    local _dir
    while read -r -d '' _dir
    do
        rm -rf "$_dir"
    done < <(find "${pkgdir}/usr/include" -mindepth 1 -maxdepth 1 -type d ! -name 'caffe*' ! -name 'c10' -print0)
    
    # license
    cd "${srcdir}/pytorch"
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -D -m644 NOTICE  -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

package_caffe2-cuda() {
    pkgdesc+=' (with cuda support)'
    depends+=('cuda' 'cudnn' 'nccl')
    provides=('caffe2')
    conflicts+=('caffe2')
    
    cd pytorch/build-cuda
    
    _package_common
}

package_caffe2() {
    pkgdesc+=' (cpu only)'
    provides=('caffe2-cpu')
    conflicts+=('caffe2-cpu')
    replaces=('caffe2-cpu')
    
    cd pytorch/build-cpu-only
    
    _package_common
}

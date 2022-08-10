# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Sven-Hendrik Haase <svenstaro@gmail.com>
# Contributor: Stephen Zhang <zsrkmyn at gmail dot com>
# Contributor: Federico Zappone <federico dot zappone at unimol dot it>

_pkgname="pytorch"
pkgbase="python-${_pkgname}-rocm"
pkgname=("${pkgbase}" "python-pytorch-opt-rocm")
pkgver=1.12.1
_pkgver=1.12.1
pkgrel=1
_pkgdesc="Tensors and Dynamic neural networks in Python with strong GPU acceleration"
pkgdesc="${_pkgdesc}"
arch=('x86_64')
url="https://pytorch.org"
license=('BSD')
depends=('google-glog' 'gflags' 'opencv' 'openmp' 'rccl' 'pybind11' 'python' 'python-yaml' 'libuv'
         'python-numpy' 'protobuf' 'ffmpeg4.4' 'python-future' 'qt5-base' 'intel-oneapi-mkl'
         'python-typing_extensions')
makedepends=('python' 'python-setuptools' 'python-yaml' 'python-numpy' 'cmake' 'rocm-hip-sdk' 'roctracer'
             'miopen' 'git' 'hipmagma' 'ninja' 'pkgconfig' 'doxygen' 'gcc11')
source=("${_pkgname}-${pkgver}::git+https://github.com/pytorch/pytorch.git#tag=v$_pkgver"
        # generated using parse-submodules
        "${pkgname}-ios-cmake::git+https://github.com/Yangqing/ios-cmake.git"
        "${pkgname}-pthreadpool::git+https://github.com/Maratyszcza/pthreadpool.git"
        "${pkgname}-NNPACK::git+https://github.com/Maratyszcza/NNPACK.git"
        "${pkgname}-psimd::git+https://github.com/Maratyszcza/psimd.git"
        "${pkgname}-FP16::git+https://github.com/Maratyszcza/FP16.git"
        "${pkgname}-FXdiv::git+https://github.com/Maratyszcza/FXdiv.git"
        "${pkgname}-cpuinfo::git+https://github.com/pytorch/cpuinfo.git"
        "${pkgname}-enum34::git+https://github.com/PeachPy/enum34.git"
        "${pkgname}-gloo::git+https://github.com/facebookincubator/gloo"
        "${pkgname}-PeachPy::git+https://github.com/malfet/PeachPy.git"
        "${pkgname}-cub::git+https://github.com/NVlabs/cub.git"
        "${pkgname}-six::git+https://github.com/benjaminp/six.git"
        "${pkgname}-QNNPACK::git+https://github.com/pytorch/QNNPACK"
        "${pkgname}-ARM_NEON_2_x86_SSE::git+https://github.com/intel/ARM_NEON_2_x86_SSE.git"
        "${pkgname}-onnx-tensorrt::git+https://github.com/onnx/onnx-tensorrt"
        "${pkgname}-ideep::git+https://github.com/intel/ideep"
        "${pkgname}-sleef::git+https://github.com/shibatch/sleef"
        "${pkgname}-foxi::git+https://github.com/houseroad/foxi.git"
        "${pkgname}-benchmark::git+https://github.com/google/benchmark.git"
        "${pkgname}-nccl::git+https://github.com/NVIDIA/nccl"
        "${pkgname}-gemmlowp::git+https://github.com/google/gemmlowp.git"
        "${pkgname}-cudnn-frontend::git+https://github.com/NVIDIA/cudnn-frontend.git"
        "${pkgname}-googletest::git+https://github.com/google/googletest.git"
        "${pkgname}-fbjni::git+https://github.com/facebookincubator/fbjni.git"
        "${pkgname}-pocketfft::git+https://github.com/mreineck/pocketfft"
        "${pkgname}-fbgemm::git+https://github.com/pytorch/fbgemm"
        "${pkgname}-tensorpipe::git+https://github.com/pytorch/tensorpipe.git"
        "${pkgname}-onnx::git+https://github.com/onnx/onnx.git"
        "${pkgname}-tbb::git+https://github.com/01org/tbb"
        "${pkgname}-fmt::git+https://github.com/fmtlib/fmt.git"
        "${pkgname}-kineto::git+https://github.com/pytorch/kineto"
        "${pkgname}-protobuf::git+https://github.com/protocolbuffers/protobuf.git"
        "${pkgname}-json::git+https://github.com/nlohmann/json.git"
        "${pkgname}-eigen::git+https://gitlab.com/libeigen/eigen.git"
        "${pkgname}-flatbuffers::git+https://github.com/google/flatbuffers.git"
        "${pkgname}-XNNPACK::git+https://github.com/google/XNNPACK.git"
        "${pkgname}-pybind11::git+https://github.com/pybind/pybind11.git"
        "${pkgname}-zstd::git+https://github.com/facebook/zstd.git"
        fix_include_system.patch
        use-system-libuv.patch
        fix-building-for-torchvision.patch
        https://patch-diff.githubusercontent.com/raw/pytorch/pytorch/pull/79360.patch
        ffmpeg4.4.patch
        "rocblas.patch::https://patch-diff.githubusercontent.com/raw/pytorch/pytorch/pull/80849.patch")
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
            '557761502bbd994d9795bef46779e4b8c60ba0b45e7d60841f477d3b7f28a00a'
            'cd9ac4aaa9f946ac5eafc57cf66c5c16b3ea7ac8af32c2558fad0705411bb669'
            '600bd6a4bbcec9f99ab815d82cee1c2875530b2b75f4010da5ba72ce9bf31aff'
            '15fee7875dc454184136df534d0450008912c83f0d74237ba5e6707db7e7914b'
            '75001b59e76831b0c93a547f851cb980e00b0d8cc7b66fb507eaeac217dc6ff9'
            'SKIP')
options=('!lto')

get_pyver () {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  cd "${srcdir}/${_pkgname}-${pkgver}"

  # generated using parse-submodules
  git submodule init

  git config submodule."third_party/pybind11".url "${srcdir}/${pkgname}"-pybind11
  git config submodule."third_party/cub".url "${srcdir}/${pkgname}"-cub
  git config submodule."third_party/eigen".url "${srcdir}/${pkgname}"-eigen
  git config submodule."third_party/googletest".url "${srcdir}/${pkgname}"-googletest
  git config submodule."third_party/benchmark".url "${srcdir}/${pkgname}"-benchmark
  git config submodule."third_party/protobuf".url "${srcdir}/${pkgname}"-protobuf
  git config submodule."third_party/ios-cmake".url "${srcdir}/${pkgname}"-ios-cmake
  git config submodule."third_party/NNPACK".url "${srcdir}/${pkgname}"-NNPACK
  git config submodule."third_party/gloo".url "${srcdir}/${pkgname}"-gloo
  git config submodule."third_party/NNPACK_deps/pthreadpool".url "${srcdir}/${pkgname}"-pthreadpool
  git config submodule."third_party/NNPACK_deps/FXdiv".url "${srcdir}/${pkgname}"-FXdiv
  git config submodule."third_party/NNPACK_deps/FP16".url "${srcdir}/${pkgname}"-FP16
  git config submodule."third_party/NNPACK_deps/psimd".url "${srcdir}/${pkgname}"-psimd
  git config submodule."third_party/zstd".url "${srcdir}/${pkgname}"-zstd
  git config submodule."third_party/cpuinfo".url "${srcdir}/${pkgname}"-cpuinfo
  git config submodule."third_party/python-enum".url "${srcdir}/${pkgname}"-enum34
  git config submodule."third_party/python-peachpy".url "${srcdir}/${pkgname}"-PeachPy
  git config submodule."third_party/python-six".url "${srcdir}/${pkgname}"-six
  git config submodule."third_party/onnx".url "${srcdir}/${pkgname}"-onnx
  git config submodule."third_party/onnx-tensorrt".url "${srcdir}/${pkgname}"-onnx-tensorrt
  git config submodule."third_party/sleef".url "${srcdir}/${pkgname}"-sleef
  git config submodule."third_party/ideep".url "${srcdir}/${pkgname}"-ideep
  git config submodule."third_party/nccl/nccl".url "${srcdir}/${pkgname}"-nccl
  git config submodule."third_party/gemmlowp/gemmlowp".url "${srcdir}/${pkgname}"-gemmlowp
  git config submodule."third_party/QNNPACK".url "${srcdir}/${pkgname}"-QNNPACK
  git config submodule."third_party/neon2sse".url "${srcdir}/${pkgname}"-ARM_NEON_2_x86_SSE
  git config submodule."third_party/fbgemm".url "${srcdir}/${pkgname}"-fbgemm
  git config submodule."third_party/foxi".url "${srcdir}/${pkgname}"-foxi
  git config submodule."third_party/tbb".url "${srcdir}/${pkgname}"-tbb
  git config submodule."android/libs/fbjni".url "${srcdir}/${pkgname}"-fbjni
  git config submodule."third_party/XNNPACK".url "${srcdir}/${pkgname}"-XNNPACK
  git config submodule."third_party/fmt".url "${srcdir}/${pkgname}"-fmt
  git config submodule."third_party/tensorpipe".url "${srcdir}/${pkgname}"-tensorpipe
  git config submodule."third_party/cudnn_frontend".url "${srcdir}/${pkgname}"-cudnn-frontend
  git config submodule."third_party/kineto".url "${srcdir}/${pkgname}"-kineto
  git config submodule."third_party/pocketfft".url "${srcdir}/${pkgname}"-pocketfft
  git config submodule."third_party/flatbuffers".url "${srcdir}/${pkgname}"-flatbuffers
  git config submodule."third_party/nlohmann".url "${srcdir}/${pkgname}"-json

  git submodule update --init --recursive

  # https://bugs.archlinux.org/task/64981
  patch -N torch/utils/cpp_extension.py "${srcdir}"/fix_include_system.patch

  # Use system libuv
  patch -Np1 -i "${srcdir}"/use-system-libuv.patch

  # fix https://github.com/pytorch/vision/issues/3695
  patch -Np1 -i "${srcdir}/fix-building-for-torchvision.patch"

  # Fix building against glog 0.6
  patch -Np1 -i "${srcdir}/79360.patch"

  # build against ffmpeg4.4
  patch -Np1 -i "${srcdir}/ffmpeg4.4.patch"

  # fix https://github.com/pytorch/pytorch/issues/80848
  patch -Np1 -i "${srcdir}/rocblas.patch"

  cd "${srcdir}"

  cp -r "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-rocm"
  cp -r "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-opt-rocm"

  export VERBOSE=1
  export PYTORCH_BUILD_VERSION="${pkgver}"
  export PYTORCH_BUILD_NUMBER=1

  # Check tools/setup_helpers/cmake.py, setup.py and CMakeLists.txt for a list of flags that can be set via env vars.
  export ATEN_NO_TEST=ON # do not build ATen tests
  export USE_MKLDNN=ON
  export BUILD_CUSTOM_PROTOBUF=OFF
  export BUILD_CAFFE2=ON
  export BUILD_CAFFE2_OPS=ON
  # export BUILD_SHARED_LIBS=OFF
  export USE_FFMPEG=ON
  export USE_GFLAGS=ON
  export USE_GLOG=ON
  export BUILD_BINARY=ON
  export USE_OBSERVERS=ON
  export USE_OPENCV=ON
  # export USE_SYSTEM_LIBS=ON  # experimental, not all libs present in repos
  export USE_SYSTEM_NCCL=ON
  export NCCL_VERSION=$(pkg-config nccl --modversion)
  export NCCL_VER_CODE=$(sed -n 's/^#define NCCL_VERSION_CODE\s*\(.*\).*/\1/p' /usr/include/nccl.h)
  # export BUILD_SPLIT_CUDA=ON  # modern preferred build, but splits libs and symbols, ABI break
  # export USE_FAST_NVCC=ON  # parallel build with nvcc, spawns too many processes
  export USE_CUPTI_SO=ON  # make sure cupti.so is used as shared lib
  export CC=/usr/bin/gcc-11
  export CXX=/usr/bin/g++-11
  export CUDAHOSTCXX=/usr/bin/g++-11
  export CUDA_HOST_COMPILER="${CUDAHOSTCXX}"
  export CUDA_HOME=/opt/cuda
  # hide buildt-time CUDA devices
  export CUDA_VISIBLE_DEVICES=""
  export CUDNN_LIB_DIR=/usr/lib
  export CUDNN_INCLUDE_DIR=/usr/include
  export TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
  export TORCH_CUDA_ARCH_LIST="5.2;6.0;6.2;7.0;7.2;7.5;8.0;8.6;8.6+PTX"  #include latest PTX for future compat
  export OVERRIDE_TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"
}

build() {
  # PYTORCH_ROCM_ARCH is an env var used to populate the PYTORCH_ROCM_ARCH export
  # PYTORCH_ROCM_ARCH="gfx908"
  # NOTE: It's your responbility to validate the value of $PYTORCH_ROCM_ARCH.
  # If unsure, don't set it and several architectures will be built.
  if [[ -n "$PYTORCH_ROCM_ARCH" ]]; then
    export PYTORCH_ROCM_ARCH="$PYTORCH_ROCM_ARCH"
  else
    export PYTORCH_ROCM_ARCH="gfx803;gfx900;gfx906;gfx908"
  fi

  echo "Building with rocm and without non-x86-64 optimizations"
  export USE_CUDA=0
  export USE_CUDNN=0
  export USE_ROCM=1
  cd "${srcdir}/${_pkgname}-${pkgver}-rocm"
  echo "add_definitions(-march=x86-64)" >> cmake/MiscCheck.cmake

  # Apply changes needed for ROCm
  python tools/amd_build/build_amd.py

  # this horrible hack is necessary because the current release
  # ships inconsistent CMake which tries to build objects before
  # thier dependencies, build twice when dependencies are available
  python setup.py build || python setup.py build

  echo "Building with rocm and with non-x86-64 optimizations"
  export USE_CUDA=0
  export USE_CUDNN=0
  export USE_ROCM=1
  cd "${srcdir}/${_pkgname}-${pkgver}-rocm"
  echo "add_definitions(-march=haswell)" >> cmake/MiscCheck.cmake

  # Apply changes needed for ROCm
  python tools/amd_build/build_amd.py

  # same horrible hack as above
  python setup.py build || python setup.py build
}

_package() {
  # Prevent setup.py from re-running CMake and rebuilding
  sed -e 's/RUN_BUILD_DEPS = True/RUN_BUILD_DEPS = False/g' -i setup.py

  python setup.py install --root="${pkgdir}"/ --optimize=1 --skip-build

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  pytorchpath="usr/lib/python$(get_pyver)/site-packages/torch"
  install -d "${pkgdir}/usr/lib"

  # put CMake files in correct place
  #mv "${pkgdir}/${pytorchpath}/share/cmake" "${pkgdir}/usr/lib/cmake"

  # put C++ API in correct place
  #mv "${pkgdir}/${pytorchpath}/include" "${pkgdir}/usr/include"
  #mv "${pkgdir}/${pytorchpath}/lib"/*.so* "${pkgdir}/usr/lib/"

  # clean up duplicates
  # TODO: move towards direct shared library dependecy of:
  #   c10, caffe2, libcpuinfo, CUDA RT, gloo, GTest, Intel MKL,
  #   NVRTC, ONNX, protobuf, libthreadpool, QNNPACK
  rm -rf "${pkgdir}/usr/include/pybind11"

  # python module is hardcoded to look there at runtime
  #ln -s /usr/include "${pkgdir}/${pytorchpath}/include"
  #find "${pkgdir}"/usr/lib -type f -name "*.so*" -print0 | while read -rd $'\0' _lib; do
  #  ln -s ${_lib#"$pkgdir"} "${pkgdir}/${pytorchpath}/lib/"
  #done
}

package_python-pytorch-rocm() {
  pkgdesc="${_pkgdesc} (with ROCM)"
  depends+=(rocm-hip-sdk roctracer miopen hipmagma)
  conflicts=(python-pytorch)
  provides=(python-pytorch)

  cd "${srcdir}/${_pkgname}-${pkgver}-rocm"
  _package
}

package_python-pytorch-opt-rocm() {
  pkgdesc="${_pkgdesc} (with ROCM and AVX2 CPU optimizations)"
  depends+=(rocm-hip-sdk roctracer miopen hipmagma)
  conflicts=(python-pytorch)
  provides=(python-pytorch python-pytorch-rocm)

  cd "${srcdir}/${_pkgname}-${pkgver}-opt-rocm"
  _package
}

# vim:set ts=2 sw=2 et:

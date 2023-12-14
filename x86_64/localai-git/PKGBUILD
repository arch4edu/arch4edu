# Maintainer: wuxxin <wuxxin@gmail.com>

# to only build for cpu, set _ENABLE_CUDA and _ENABLE_ROCM to 0
_ENABLE_CUDA=${_ENABLE_CUDA:-1}
_ENABLE_ROCM=${_ENABLE_ROCM:-1}
_SKIP_CPU=${_SKIP_CPU:-0}
# list of amd gfx architectures to build if GPU_TARGETS and AMDGPU_TARGETS are empty
_AMDGPU_TARGETS="gfx900;gfx906;gfx908;gfx90a;gfx1030;gfx1100;gfx1101;gfx1102"
if test -n "$GPU_TARGETS"; then _AMDGPU_TARGETS="$GPU_TARGETS"; fi
if test -n "$AMDGPU_TARGETS"; then _AMDGPU_TARGETS="$AMDGPU_TARGETS"; fi
_GO_TAGS=""
# _GO_TAGS="tts stablediffusion"
_OPTIONAL_BACKENDS=""
if test -n "$(echo "$_GO_TAGS" | grep -o "tts")"; then
  _OPTIONAL_BACKENDS="backend-assets/grpc/piper $_OPTIONAL_BACKENDS"
fi
if test -n "$(echo "$_GO_TAGS" | grep -o "stablediffusion")"; then
  _OPTIONAL_BACKENDS="backend-assets/grpc/stablediffusion $_OPTIONAL_BACKENDS"
fi
# list of backends to be build
_GRPC_BACKENDS="backend-assets/grpc/llama-cpp backend-assets/grpc/whisper $_OPTIONAL_BACKENDS backend-assets/grpc/bert-embeddings"
# optional args for main Makefile calling
_OPTIONAL_MAKE_ARGS="$_OPTIONAL_MAKE_ARGS"
_pkgname="localai"

pkgbase="${_pkgname}-git"
pkgname=("${pkgbase}")
pkgver=v2.0.0.28.g7641f92
pkgrel=2
pkgdesc="Self-hosted OpenAI API alternative - Open Source, community-driven and local-first."
url="https://github.com/mudler/LocalAI"
license=('MIT')
arch=('x86_64')

provides=('localai')
conflicts=('localai')

depends=(
)
makedepends=(
  'go'
  'git'
  'cmake'
  'grpc'
  'opencv'
  'blas-openblas'
  'sdl2'
  'ffmpeg'
)

if test "$(echo "$_GO_TAGS" | grep -o "tts")" = "tts"; then
  makedepends+=(
    'onnxruntime'
  )
  # 'piper-phonemize' is build from piper
fi

if [[ $_ENABLE_CUDA = 1 ]]; then
  pkgname+=("${pkgbase}-cuda")
  makedepends+=(
    'cuda'
    'cudnn'
    'nccl'
    'magma-cuda'
  )
fi

if [[ $_ENABLE_ROCM = 1 ]]; then
  pkgname+=("${pkgbase}-rocm")
  makedepends+=(
    'rocm-hip-sdk'
    'miopen-hip'
    'rccl'
    'magma-hip'
  )
fi

source=(
  "${_pkgname}"::"git+https://github.com/mudler/LocalAI"
)

sha256sums=(
  'SKIP'
)

pkgver() {
  cd "${srcdir}/${_pkgname}"
  (git describe --always --tags | tr "-" ".")
}

prepare() {
  cd "${srcdir}/${_pkgname}"

  if test -n "$_OPTIONAL_MAKE_ARGS"; then
    echo "_OPTIONAL_MAKE_ARGS=$_OPTIONAL_MAKE_ARGS"
  fi

  # fix LLAMA_VERSION not set from CPPLLAMA_VERSION in llama.cpp build
  sed -ri 's#^(\t+)(LLAMA_VERSION=\$\(CPPLLAMA_VERSION\) +)(\$\(MAKE\) -C backend/cpp/llama +)(grpc-server.*)#\1\3\2\4#g' Makefile
  sed -ri 's#^(\t+\$\(MAKE\) -C backend/cpp/llama +)(llama.cpp.*$)#\1LLAMA_VERSION=$(CPPLLAMA_VERSION) \2#g' Makefile

  # fix deprecated memory_f16 in gpt_params
  sed -ri 's#[ \t]+params.memory_f16 = request->f16memory\(\);[ \t]*##g' backend/cpp/llama/grpc-server.cpp

  # modify get-sources
  _EXTERNAL_SOURCES="backend/cpp/llama/llama.cpp sources/go-piper sources/whisper.cpp sources/go-bert"
  sed -ri "s#get-sources: .*#get-sources: $_EXTERNAL_SOURCES#g" Makefile

  # remove go mod edits for inactive backend sources
  sed -ri 's#.+\-replace github.com/nomic-ai/gpt4all/gpt4all.+##g' Makefile
  sed -ri 's#.+\-replace github.com/donomii/go-rwkv.cpp.+##g' Makefile
  sed -ri 's#.+\-replace github.com/go-skynet/go-ggml-transformers.cpp.+##g' Makefile
  sed -ri 's#.+\-replace github.com/mudler/go-stable-diffusion.+##g' Makefile

  # fetch sources of backends to be recursive git checked out before build()
  mkdir -p "sources"
  make $_OPTIONAL_MAKE_ARGS $_EXTERNAL_SOURCES

  # # fix stablediffusion
  # sed -ri "s/^(#include <ncnn\/)(benchmark|net)(\.h>)/\1src\/\2\3/g" \
  #   sources/go-stable-diffusion/stablediffusion.hpp

  # copy for different build types
  cd "${srcdir}"
  for n in "${_pkgname}-cpu" "${_pkgname}-cuda" "${_pkgname}-rocm"; do
    if test -d "$n"; then rm -rf "$n"; fi
    cp -r "${_pkgname}" "$n"
  done

  # ROCM workarounds
  cd "${srcdir}/${_pkgname}-rocm"
  # workaround build error on ROCM by removing unsupported cf-protection from CMAKE_CXX_FLAGS
  sed -i '1s/^/string(REPLACE "-fcf-protection" "" CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")\n/' \
    backend/cpp/llama/llama.cpp/CMakeLists.txt
  # workaround --offload-arch for multiple GPU_TARGETS, makefile does "," splitting, data is ";"
  #      also: --ofload-arch is deprecated, replace it with -DGPU_TARGETS
  for i in backend/cpp/llama/llama.cpp/Makefile sources/whisper.cpp/Makefile; do
    sed -ri 's/^(.+HIPFLAGS.+\+=).+offload-arch=.+$/\1 -DGPU_TARGETS="$(GPU_TARGETS)"/g' "$i"
  done
}

_build() {
  if test -n "$(echo "$_GO_TAGS" | grep -o "stablediffusion")"; then
    make BUILD_TYPE="$1" GRPC_BACKENDS="backend-assets/grpc/stablediffusion" GO_TAGS="$_GO_TAGS" $_OPTIONAL_MAKE_ARGS build
  fi
  make BUILD_TYPE="$1" GRPC_BACKENDS="$_GRPC_BACKENDS" GO_TAGS="$_GO_TAGS" $_OPTIONAL_MAKE_ARGS build
}

build() {
  if test "$_SKIP_CPU" != "1"; then
    cd "${srcdir}/${_pkgname}-cpu"
    _build openblas
  fi

  if [[ $_ENABLE_CUDA = 1 ]]; then
    cd "${srcdir}/${_pkgname}-cuda"
    export CUDA_HOME="${CUDA_HOME:-/opt/cuda}"
    export PATH="$CUDA_HOME/bin:$PATH"
    MAGMA_HOME="$CUDA_HOME/targets/x86_64-linux" CUDA_LIBPATH="$CUDA_HOME/lib64/" \
      _build cublas
  fi

  if [[ $_ENABLE_ROCM = 1 ]]; then
    cd "${srcdir}/${_pkgname}-rocm"
    export ROCM_HOME="${ROCM_HOME:-/opt/rocm}"
    export PATH="$ROC_HOME/bin:$PATH"
    MAGMA_HOME="$ROCM_HOME" AMDGPU_TARGETS="$_AMDGPU_TARGETS" GPU_TARGETS="$_AMDGPU_TARGETS" \
      _build hipblas
  fi
}

_package_install() {
  install -Dm755 "local-ai" "${pkgdir}/usr/bin/local-ai"
  install -Dm644 README.md -t "${pkgdir}/usr/share/doc/${_pkgname}"
}

package_localai-git() {
  if test "$_SKIP_CPU" != "1"; then
    cd "${srcdir}/${_pkgname}-cpu"
    _package_install
  fi
}

package_localai-git-cuda() {
  cd "${srcdir}/${_pkgname}-cuda"
  pkgdesc+=' (with CUDA support)'
  depends+=('cuda')
  _package_install
}

package_localai-git-rocm() {
  cd "${srcdir}/${_pkgname}-rocm"
  pkgdesc+=' (with ROCM support)'
  depends+=('rocm-hip-runtime')
  _package_install
}

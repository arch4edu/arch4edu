# Maintainer: wuxxin <wuxxin@gmail.com>

# to only build for cpu, set ENABLE_CUDA and ENABLE_ROCM to 0
_ENABLE_CUDA=1
_ENABLE_ROCM=0
_SKIP_CPU=0
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
_GRPC_BACKENDS="backend-assets/grpc/bert-embeddings backend-assets/grpc/llama-cpp backend-assets/grpc/whisper $_OPTIONAL_BACKENDS"
_pkgname="localai"

pkgbase="${_pkgname}-git"
pkgname=("${pkgbase}")
pkgver=v2.0.0.6.g997119c
pkgrel=1
pkgdesc="The free, Open Source OpenAI alternative. Self-hosted, community-driven and local-first."
url="https://github.com/mudler/LocalAI"
license=('MIT')
arch=('x86_64')

provides=('localai')
conflicts=('localai')

depends=(
  'grpc'
  'opencv'
  'blas-openblas'
  'sdl2'
  'ffmpeg'
)
makedepends=(
  'go'
  'git'
  'cmake'
)

if test "$(echo "$_GO_TAGS" | grep -o "tts")" = "tts"; then
  depends+=(
    'onnxruntime'
    'piper-phonemize'
  )
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

  # list of backend sources to be recursive git checked out before build()
  _EXTERNAL_SOURCES="backend/cpp/llama/llama.cpp sources/go-piper sources/whisper.cpp sources/go-bert"
  # fetch sources for active backends
  mkdir -p "sources"
  make $_EXTERNAL_SOURCES

  # modify get-sources, remove go mod edits for inactive backend sources
  sed -ri "s#get-sources: .*#get-sources: $_EXTERNAL_SOURCES#g" Makefile
  sed -ri 's#.+\-replace github.com/nomic-ai/gpt4all/gpt4all.+##g' Makefile
  sed -ri 's#.+\-replace github.com/donomii/go-rwkv.cpp.+##g' Makefile
  sed -ri 's#.+\-replace github.com/go-skynet/go-ggml-transformers.cpp.+##g' Makefile
  sed -ri 's#.+\-replace github.com/mudler/go-stable-diffusion.+##g' Makefile

  # # patch stablediffusion
  # sed -ri "s/^(#include <ncnn\/)(benchmark|net)(\.h>)/\1src\/\2\3/g" \
  #   sources/go-stable-diffusion/stablediffusion.hpp

  # copy for different build types
  cd "${srcdir}"
  for n in "${_pkgname}-cpu" "${_pkgname}-cuda" "${_pkgname}-rocm"; do
    if test -d "$n"; then rm -rf "$n"; fi
    cp -r "${_pkgname}" "$n"
  done
}

_build() {
  if test -n "$(echo "$_GO_TAGS" | grep -o "stablediffusion")"; then
    make BUILD_TYPE="$1" GRPC_BACKENDS="backend-assets/grpc/stablediffusion" GO_TAGS="$_GO_TAGS" build
  fi
  make BUILD_TYPE="$1" GRPC_BACKENDS="$_GRPC_BACKENDS" GO_TAGS="$_GO_TAGS" build
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
    if test -n "$GPU_TARGETS"; then
      _AMDGPU_TARGETS="$GPU_TARGETS"
    else
      _AMDGPU_TARGETS="${AMDGPU_TARGETS:-gfx900;gfx906;gfx908;gfx90a;gfx1030;gfx1100;gfx1101;gfx1102}"
    fi
    MAGMA_HOME="$ROCM_HOME" AMDGPU_TARGETS="$_AMDGPU_TARGETS" GPU_TARGETS="$_AMDGPU_TARGETS" \
      _build hipblas
  fi
}

_package_install() {
  install -Dm755 "local-ai" "${pkgdir}/usr/bin/local-ai"
  # sources/go-piper/piper/build/pi/lib/* /usr/lib/

  # add 1-2 7b high performing models yaml configs based on mistral as gpt-3.5
  # prefer chatml, add example working preload-models.yaml,

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

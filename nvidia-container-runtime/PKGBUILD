# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

pkgver=2.0.0+3.docker18.09.6
_runtime_commit='03af0a80dbcbcfa09a828cde46151749bee2480e'
_runc_commit='2b18fe1d885ee5083ef9f0838fee39b62d653e30'
_runc_patch_commit='6635b4f0c6af3810594d2770f662f34ddc15b40d'
_runc_path='gopath/src/github.com/opencontainers/runc'

pkgrel=1
pkgdesc='NVIDIA container runtime'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('BSD')

makedepends=('go' 'git')
depends=('libseccomp' 'nvidia-container-runtime-hook')

source=("git+https://github.com/NVIDIA/nvidia-container-runtime.git#commit=${_runtime_commit}"
        "git+https://github.com/opencontainers/runc.git#commit=${_runc_commit}")
sha256sums=('SKIP'
            'SKIP')

prepare() {
  cd runc
  git apply ${srcdir}/nvidia-container-runtime/runtime/runc/${_runc_patch_commit}/*
  mkdir -p ${srcdir}/gopath/src/github.com/opencontainers
  ln -rTsf "${srcdir}/runc" "${srcdir}/${_runc_path}"
}

build() {
  cd ${srcdir}/${_runc_path}
  GOPATH="${srcdir}/gopath" EXTRA_LDFLAGS="-extldflags=-Wl,-z,now,-z,relro" make
}

package() {
  install -D -m755 "${srcdir}/${_runc_path}/runc" "$pkgdir/usr/bin/nvidia-container-runtime"
  install -D -m644 "${srcdir}/nvidia-container-runtime/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.0.5
pkgrel=3
_runtime_pkgver=3.1.4

pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('BSD')

makedepends=('go')
depends=('libnvidia-container-tools' 'docker>=1:19.03')
conflicts=('nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')

source=("https://github.com/NVIDIA/nvidia-container-runtime/archive/v${_runtime_pkgver}.tar.gz")
sha256sums=('32bd9f49a1392253dccbfebc850b980b6d7cbd1b2621b06ced4fbe952c918038')

_srcdir="nvidia-container-runtime-${_runtime_pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/toolkit/${pkgname}" "gopath/src/$pkgname"
}

build() {
  GOPATH="${srcdir}/gopath" go build -v \
                            -buildmode=pie \
                            -gcflags "all=-trimpath=${PWD}" \
                            -asmflags "all=-trimpath=${PWD}" \
                            -ldflags "-extldflags ${LDFLAGS}" \
                            "$pkgname"
                            # -trimpath \  # only go > 1.13
                            #-ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" \
}

package() {
  install -D -m755 "${srcdir}/${pkgname}" "$pkgdir/usr/bin/${pkgname}"
  pushd "$pkgdir/usr/bin/"
  ln -sf "${pkgname}" "nvidia-container-runtime-hook"
  popd
  install -D -m644 "${_srcdir}/toolkit/config.toml.centos" "$pkgdir/etc/nvidia-container-runtime/config.toml"

  install -D -m644 "${_srcdir}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

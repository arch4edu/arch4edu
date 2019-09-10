# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-toolkit

pkgver=1.0.4
_runtime_pkgver=3.1.3

pkgrel=1
pkgdesc='NVIDIA container runtime toolkit'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('BSD')

makedepends=('go')
depends=('libnvidia-container-tools' 'docker>=1:19.03')
conflicts=('nvidia-container-runtime-hook' 'nvidia-container-runtime<2.0.0')
replaces=('nvidia-container-runtime-hook')

source=("https://github.com/NVIDIA/nvidia-container-runtime/archive/v${_runtime_pkgver}.tar.gz")
sha256sums=('d2eef8256d1499708c5d40eb42d8e4b389e2f62f47466bca1bc5ae927b750674')

_srcdir="nvidia-container-runtime-${_runtime_pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/toolkit/${pkgname}" "gopath/src/$pkgname"
}

build() {
  GOPATH="${srcdir}/gopath" go install \
                            -buildmode=pie \
                            -gcflags "all=-trimpath=${PWD}" \
                            -asmflags "all=-trimpath=${PWD}" \
                            -ldflags "-extldflags ${LDFLAGS}" \
                            "$pkgname"
                            #-ldflags " -s -w -extldflags=-Wl,-z,now,-z,relro" \
}

package() {
  install -D -m755 "${srcdir}/gopath/bin/${pkgname}" "$pkgdir/usr/bin/${pkgname}"
  pushd "$pkgdir/usr/bin/"
  ln -sf "${pkgname}" "nvidia-container-runtime-hook"
  popd
  install -D -m644 "${_srcdir}/toolkit/config.toml.centos" "$pkgdir/etc/nvidia-container-runtime/config.toml"

  install -D -m644 "${_srcdir}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

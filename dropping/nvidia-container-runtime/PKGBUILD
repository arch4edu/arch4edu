# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Julie Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

pkgver=3.5.0
pkgrel=2

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('APACHE')

makedepends=('go')
depends=('libseccomp' 'nvidia-container-toolkit>=1.5.0')

source=("https://github.com/NVIDIA/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('4985efe4488e441d0e4910cc7eb2046176db063e5bbe2e0542a7c08d5c5e7d34')

_srcdir="${pkgname}-${pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/src" "gopath/src/${pkgname}"
}

build() {
  cd "${_srcdir}"
  pwd
  make build
  #go build \
  #    -buildmode=pie \
  #    -gcflags "all=-trimpath=${PWD}" \
  #    -asmflags "all=-trimpath=${PWD}" \
  #    -ldflags "-extldflags ${LDFLAGS}"
}

package() {
  install -D -m755 "${srcdir}/${_srcdir}/nvidia-container-runtime" "${pkgdir}/usr/bin/nvidia-container-runtime"
  install -D -m644 "${srcdir}/${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

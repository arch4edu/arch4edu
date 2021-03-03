# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

pkgver=3.4.2
pkgrel=2

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('APACHE')

makedepends=('go')
depends=('libseccomp' 'nvidia-container-toolkit>=1.4.2')

source=("https://github.com/NVIDIA/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('30e8a871b4cd8e1577d9439ae4f17fa9208f8f7c026ad69c8e41e3e3d103a38b')

_srcdir="${pkgname}-${pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/src" "gopath/src/${pkgname}"
}

build() {
  cd "${_srcdir}/src"
  pwd
  go build \
      -buildmode=pie \
      -gcflags "all=-trimpath=${PWD}" \
      -asmflags "all=-trimpath=${PWD}" \
      -ldflags "-extldflags ${LDFLAGS}"
}

package() {
  install -D -m755 "${srcdir}/${_srcdir}/src/container-runtime" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${srcdir}/${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

pkgver=3.1.2
pkgrel=1

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('BSD')

makedepends=('go' 'git')
depends=('libseccomp' 'nvidia-container-toolkit<2.0.0')

source=("https://github.com/NVIDIA/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('ccc2f60ae46765c9529b1c419365445d56e939d6bbbabd755d3c6175d7d22dc5')

_srcdir="${pkgname}-${pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/runtime/src" "gopath/src/${pkgname}"
}

build() {
  GOPATH="${srcdir}/gopath" go install -buildmode=pie \
                            -gcflags "all=-trimpath=${PWD}" \
                            -asmflags "all=-trimpath=${PWD}" \
                            -ldflags "-extldflags ${LDFLAGS}" \
                            "$pkgname"
}

package() {
  install -D -m755 "${srcdir}/gopath/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${srcdir}/${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

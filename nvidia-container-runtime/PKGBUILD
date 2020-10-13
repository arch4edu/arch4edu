# Maintainer: Kien Dang <mail at kien dot ai>
# Maintainer: Joel Shapiro <jshapiro at nvidia dot com>

pkgname=nvidia-container-runtime

pkgver=3.4.0
pkgrel=1

pkgdesc='NVIDIA opencontainer runtime fork to expose GPU devices to containers.'
arch=('x86_64')
url='https://github.com/NVIDIA/nvidia-container-runtime'
license=('APACHE')

makedepends=('go')
depends=('libseccomp' 'nvidia-container-toolkit>=1.3.0')

source=("https://github.com/NVIDIA/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('bc27c35717cf5c50fc17a7066e34dcd2dac2cb4165cc14b551d6ac20f15998c4')

_srcdir="${pkgname}-${pkgver}"

prepare() {
  mkdir -p gopath/src
  ln -rTsf "${_srcdir}/src" "gopath/src/${pkgname}"
}

build() {
  GOPATH="${srcdir}/gopath" go install \
                            -buildmode=pie \
                            -gcflags "all=-trimpath=${PWD}" \
                            -asmflags "all=-trimpath=${PWD}" \
                            -ldflags "-extldflags ${LDFLAGS}" \
                            "$pkgname"
}

package() {
  install -D -m755 "${srcdir}/gopath/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -D -m644 "${srcdir}/${_srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

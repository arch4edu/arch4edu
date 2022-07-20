# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ca
_pkgver=0.71.1
pkgname=r-${_pkgname,,}
pkgver=0.71.1
pkgrel=7
pkgdesc='Simple, Multiple and Joint Correspondence Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-rgl
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('040c2fc94c356075f116cc7cd880530b3c9e02206c0035182c03a525ee99b424')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

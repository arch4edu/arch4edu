# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Rspc
_pkgver=1.2.2
pkgname=r-${_pkgname,,}
pkgver=1.2.2
pkgrel=5
pkgdesc='Nelson Rules for Control Charts'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-knitr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9e78d619e09bf1fb210dab1cd6cc424ac537706a91b0168a763c0100edc5dfb2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

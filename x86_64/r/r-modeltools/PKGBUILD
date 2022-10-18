# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributorr: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=modeltools
_pkgver=0.2-23
pkgname=r-${_pkgname,,}
pkgver=0.2.23
pkgrel=10
pkgdesc='Tools and Classes for Statistical Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6b3e8d5af1a039db5c178498dbf354ed1c5627a8cea9229726644053443210ef')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

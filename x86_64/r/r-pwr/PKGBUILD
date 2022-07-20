# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pwr
_pkgver=1.3-0
pkgname=r-${_pkgname,,}
pkgver=1.3.0
pkgrel=4
pkgdesc='Basic Functions for Power Analysis'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
optdepends=(
  r-ggplot2
  r-knitr
  r-rmarkdown
  r-scales
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('5bb00747aa599b11f133e94c6e4999e592456e966cba3607bbd1fcb1c7f1dfcd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

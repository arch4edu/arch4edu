# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=keras
_pkgver=2.11.1
pkgname=r-${_pkgname,,}
pkgver=2.11.1
pkgrel=1
pkgdesc="R Interface to 'Keras'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-generics
  r-glue
  r-magrittr
  r-r6
  r-reticulate
  r-rlang
  r-tensorflow
  r-tfruns
  r-zeallot
)
optdepends=(
  r-callr
  r-ggplot2
  r-jpeg
  r-knitr
  r-png
  r-rmarkdown
  r-testthat
  r-tfdatasets
  r-withr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('195587d5beae607345b43b118f29c18de53fe65414bc2f3a2084a2c534447740')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

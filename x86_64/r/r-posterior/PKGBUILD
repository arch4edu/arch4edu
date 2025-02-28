# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=posterior
_pkgver=1.6.1
pkgname=r-${_pkgname,,}
pkgver=1.6.1
pkgrel=1
pkgdesc='Tools for Working with Posterior Distributions'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('BSD')
depends=(
  r
  r-abind
  r-checkmate
  r-distributional
  r-matrixstats
  r-pillar
  r-rlang
  r-tensora
  r-tibble
  r-vctrs
)
optdepends=(
  r-caret
  r-dplyr
  r-e1071
  r-gbm
  r-ggplot2
  r-knitr
  r-randomforest
  r-rmarkdown
  r-testthat
  r-tidyr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e507d7bd3f4c9f542cb2ec89bc38d01bd05f9864461533fe4ba8bb8a9e7ba799')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=posterior
_pkgver=1.5.0
pkgname=r-${_pkgname,,}
pkgver=1.5.0
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
sha256sums=('4a10307fcae321f2cd4ca7871504a0c6c9152b8473dc9a033721e8dcda18e2de')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

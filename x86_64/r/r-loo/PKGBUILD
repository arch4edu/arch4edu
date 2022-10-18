# system requirements: pandoc (>= 1.12.3), pandoc-citeproc
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com


_pkgname=loo
_pkgver=2.5.1
pkgname=r-${_pkgname,,}
pkgver=2.5.1
pkgrel=6
pkgdesc='Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-checkmate
  r-matrixstats
  pandoc
)
optdepends=(
  r-bayesplot
  r-brms
  r-ggplot2
  r-graphics
  r-knitr
  r-rmarkdown
  r-rstan
  r-rstanarm
  r-rstantools
  r-spdep
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('866a2f54a4e8726cc3062e27daa8a073e6ac4aeb6719af7845284f7a668745f1')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

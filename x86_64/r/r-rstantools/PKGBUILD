# system requirements: pandoc, C++14
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rstantools
_pkgver=2.3.0
pkgname=r-${_pkgname,,}
pkgver=2.3.0
pkgrel=1
pkgdesc="Tools for Developing R Packages Interfacing with 'Stan'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-desc
  r-rcpp
  r-rcppparallel
)
optdepends=(
  r-knitr
  r-pkgbuild
  r-pkgload
  r-rmarkdown
  r-roxygen2
  r-rstan
  r-rstudioapi
  r-testthat
  r-usethis
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('937e2de6ac80214dccd90c09b26ebcf366c4b55adc84837a6fbb137ebb13822d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

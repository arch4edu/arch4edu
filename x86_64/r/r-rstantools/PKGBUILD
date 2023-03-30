# system requirements: pandoc, C++14
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rstantools
_pkgver=2.3.1
pkgname=r-${_pkgname,,}
pkgver=2.3.1
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
sha256sums=('82d4f2e884ffc894463bd37765606d5a9bef2ee631758840ec58636acdca6975')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

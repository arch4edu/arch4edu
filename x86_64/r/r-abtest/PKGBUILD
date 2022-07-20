# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=abtest
_pkgver=1.0.1
pkgname=r-${_pkgname,,}
pkgver=1.0.1
pkgrel=4
pkgdesc='Bayesian A/B Testing'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mvtnorm
  r-plotrix
  r-qgam
  r-rcolorbrewer
  r-rcpp
  r-sn
  r-truncnorm
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0f3b2952fb5892cc564acf691543eb97766499d74595493b82e812338acfe24b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

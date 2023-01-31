# system requirements: GNU make
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=cubature
_pkgver=2.0.4.6
pkgname=r-${_pkgname,,}
pkgver=2.0.4.6
pkgrel=1
pkgdesc='Adaptive Multivariate Integration over Hypercubes'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  make
)
optdepends=(
  r-benchr
  r-knitr
  r-mvtnorm
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('330c9dc2be9bf6815473fd40efa8c2de47c1ed286cb097d0ff846b56c9e9f95a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bain
_pkgver=0.2.10
pkgname=r-${_pkgname,,}
pkgver=0.2.10
pkgrel=1
pkgdesc='Bayes Factors for Informative Hypotheses'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-lavaan
)
optdepends=(
  r-knitr
  r-mass
  r-rmarkdown
  r-testthat
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('50559e9b09e21440499370b4a2080447278d35908f64930fb17eb7d72cf9d3ce')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

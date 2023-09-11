# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bain
_pkgver=0.2.9
pkgname=r-${_pkgname,,}
pkgver=0.2.9
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
sha256sums=('77c4c45b36ba472a6c1b44787e58c366b82287d0c0e0335004bbbff01dbb92ed')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

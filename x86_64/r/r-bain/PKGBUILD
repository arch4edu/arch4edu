# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=bain
_pkgver=0.2.11
pkgname=r-${_pkgname,,}
pkgver=0.2.11
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
sha256sums=('8c7a8b07bc954231372c4551a5898ec21c8a9451f2ae14c4c107c534e208f18c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

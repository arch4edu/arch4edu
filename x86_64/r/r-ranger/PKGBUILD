# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ranger
_pkgver=0.15.1
pkgname=r-${_pkgname,,}
pkgver=0.15.1
pkgrel=1
pkgdesc='A Fast Implementation of Random Forests'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-survival
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4d65d9ee7c5f2704a0e303a27222c02aa53e49f3c28dc0b4451371e37ada2b2e')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

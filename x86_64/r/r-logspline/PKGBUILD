# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logspline
_pkgver=2.1.19
pkgname=r-${_pkgname,,}
pkgver=2.1.19
pkgrel=1
pkgdesc='Routines for Logspline Density Estimation'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('Apache')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('37219e6edfdee59d8edee96ca1cb97902905ae049a7a921fbab2e162ad654794')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

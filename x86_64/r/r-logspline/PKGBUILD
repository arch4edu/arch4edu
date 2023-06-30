# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=logspline
_pkgver=2.1.20
pkgname=r-${_pkgname,,}
pkgver=2.1.20
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
sha256sums=('8bbd4b5126b597fb274be83b89ce0ff8bf0b3145649e0ea4130f27a8d37f59db')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

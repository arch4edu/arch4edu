# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=partitions
_pkgver=1.10-4
pkgname=r-${_pkgname,,}
pkgver=1.10.4
pkgrel=5
pkgdesc='Additive Partitions of Integers'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gmp
  r-mathjaxr
  r-polynom
  r-sets
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b10091416c3453eb9e9fd46c8cdd35668236579676db43d0267d79e7856467c6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

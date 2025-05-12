# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=partitions
_pkgver=1.10-9
pkgname=r-${_pkgname,,}
pkgver=1.10.9
pkgrel=1
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
  r-rdpack
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1a2dcded62592508932138d5233b6acd21fdde128dd55c907e07464a42ad1c21')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

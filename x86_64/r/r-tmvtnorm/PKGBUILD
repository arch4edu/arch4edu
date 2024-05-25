# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tmvtnorm
_pkgver=1.6
pkgname=r-${_pkgname,,}
pkgver=1.6
pkgrel=1
pkgdesc='Truncated Multivariate Normal and Student t Distribution'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-gmm
  r-mvtnorm
)
optdepends=(
  r-lattice
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2d9b2c5330d11a62384b4c0c1c012be34806b48683898045a4a40fdb9a8e1bba')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

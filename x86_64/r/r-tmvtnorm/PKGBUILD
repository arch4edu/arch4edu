# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tmvtnorm
_pkgver=1.7
pkgname=r-${_pkgname,,}
pkgver=1.7
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
sha256sums=('4b180b31e3bc4eb5009f5d7d83b7f2dd377989341ef27502113127d60f531bd8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

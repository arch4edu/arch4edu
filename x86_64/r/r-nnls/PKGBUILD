# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nnls
_pkgver=1.5
pkgname=r-${_pkgname,,}
pkgver=1.5
pkgrel=1
pkgdesc='The Lawson-Hanson algorithm for non-negative least squares (NNLS)'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cd70feb286f86f6dead75da693a8f67c9bd3b91eb738e6e6ac659e3b8c7a3452')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nnls
_pkgver=1.4
pkgname=r-${_pkgname,,}
pkgver=1.4
pkgrel=4
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
sha256sums=('0e5d77abae12bc50639d34354f96a8e079408c9d7138a360743b73bd7bce6c1f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

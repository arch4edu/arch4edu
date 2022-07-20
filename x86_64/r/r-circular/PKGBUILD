# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=circular
_pkgver=0.4-95
pkgname=r-${_pkgname,,}
pkgver=0.4.95
pkgrel=1
pkgdesc='Circular Statistics'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mvtnorm
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('483d3e31e9c7afe59e6bcb98ad17c4f6333d19b6c70f948b168c9ee16e90bce2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

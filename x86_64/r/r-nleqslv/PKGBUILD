# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nleqslv
_pkgver=3.3.5
pkgname=r-${_pkgname,,}
pkgver=3.3.5
pkgrel=1
pkgdesc='Solve Systems of Nonlinear Equations'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('1298172d2fe67d8d6b742ce7e792f6b897f081da5c94d34f14970ab531f04b3a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

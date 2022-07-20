# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=glasso
_pkgver=1.11
pkgname=r-${_pkgname,,}
pkgver=1.11
pkgrel=4
pkgdesc='Graphical Lasso: Estimation of Gaussian Graphical Models'
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
sha256sums=('4c37844b26f55985184a734e16b8fe880b192e3d2763614b0ab3f99b4530e30a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

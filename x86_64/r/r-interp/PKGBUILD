# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=interp
_pkgver=1.1-5
pkgname=r-${_pkgname,,}
pkgver=1.1.5
pkgrel=1
pkgdesc='Interpolation Methods'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-deldir
  r-rcpp
  r-rcppeigen)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-deriv
  r-ggplot2
  r-gridextra
  r-lattice
  r-mass
  r-rcppeigen
  r-ryacas
  r-scatterplot3d
  r-sp
  r-stringi
  r-stringr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0c520971a10156162e4430873066e73b798be2f45aa0f222d64c987aba0e4b20')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

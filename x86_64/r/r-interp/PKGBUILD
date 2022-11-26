# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=interp
_pkgver=1.1-3
pkgname=r-${_pkgname,,}
pkgver=1.1.3
pkgrel=4
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
  r-rcppeigen
  r-ryacas
  r-sp
  r-stringi
  r-stringr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b74e606b38cfb02985c1f9e3e45093620f76c0307b1b0b4058761e871eb5fa3f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

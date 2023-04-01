# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=interp
_pkgver=1.1-4
pkgname=r-${_pkgname,,}
pkgver=1.1.4
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
  r-rcppeigen
  r-ryacas
  r-sp
  r-stringi
  r-stringr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4f7b5d388132a4d76e8635e2a7c4fa0d705df2b49e7d108faa16ce2236e34d06')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

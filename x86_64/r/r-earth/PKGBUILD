# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=earth
_pkgver=5.3.6
pkgname=r-${_pkgname,,}
pkgver=5.3.6
pkgrel=1
pkgdesc='Multivariate Adaptive Regression Splines'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-formula
  r-plotmo
  r-teachingdemos
)
optdepends=(
  r-gam
  r-mass
  r-mda
  r-mgcv
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('caa8398705b3eb5d6e8972ab801596f177a30e8de8b821eea2cfbf26568c9fbd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

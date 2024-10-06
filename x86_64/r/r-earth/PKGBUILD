# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=earth
_pkgver=5.3.4
pkgname=r-${_pkgname,,}
pkgver=5.3.4
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
sha256sums=('3af94f925598fa2be7d320ad5365e285c008933cc0198a33b8149fdbaae6debc')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

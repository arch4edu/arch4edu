# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rockchalk
_pkgver=1.8.152
pkgname=r-${_pkgname,,}
pkgver=1.8.152
pkgrel=4
pkgdesc='Regression Estimation and Presentation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cardata
  r-kutils
  r-lme4
)
optdepends=(
  r-car
  r-hh
  r-hmisc
  r-mvtnorm
  r-scatterplot3d
  r-tables
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('031acb78612fa5da7d33530ee6d392aa540ef327ad35c5a2dab70ccf1e9525b4')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

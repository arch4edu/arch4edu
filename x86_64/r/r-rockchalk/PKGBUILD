# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=rockchalk
_pkgver=1.8.164
pkgname=r-${_pkgname,,}
pkgver=1.8.164
pkgrel=1
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
sha256sums=('5c8e071eee7cc6bc22b43fd4ac9681182a3167191d372ee124912b87555d4d16')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=scatterplot3d
_pkgver=0.3-41
pkgname=r-${_pkgname,,}
pkgver=0.3.41
pkgrel=4
pkgdesc='3D Scatter Plot'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4c8326b70a3b2d37126ca806771d71e5e9fe1201cfbe5b0d5a0a83c3d2c75d94')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

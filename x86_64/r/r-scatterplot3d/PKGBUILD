# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=scatterplot3d
_pkgver=0.3-43
pkgname=r-${_pkgname,,}
pkgver=0.3.43
pkgrel=1
pkgdesc='3D Scatter Plot'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('90d7bfb535b76008768306ea9209adfb48e0e07f36eabbb59ab6ddb6522f16a5')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=scatterplot3d
_pkgver=0.3-42
pkgname=r-${_pkgname,,}
pkgver=0.3.42
pkgrel=1
pkgdesc='3D Scatter Plot'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a9fedde70e1a846c4dcafbff20f115425206d507896d12c2b21ff052556c5216')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

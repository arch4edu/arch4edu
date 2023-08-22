# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2023.8-1
pkgname=r-${_pkgname,,}
pkgver=2023.8.1
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e445d479e477e2d42daac1d7f7db0daf6628aac6b3f8a2d51dbb95b4ad1ecfeb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

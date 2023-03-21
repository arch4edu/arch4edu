# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2023.3-1
pkgname=r-${_pkgname,,}
pkgver=2023.3.1
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('8748086c3d45286b7c9a81f0f8e58df75a09ba555d48a6eb8cd94af0c7c92a26')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2023.11-1
pkgname=r-${_pkgname,,}
pkgver=2023.11.1
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('e2d71c2ee4696dc39e44b58099be5d5dc8bf0600cc663315ee76f33884354b3f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

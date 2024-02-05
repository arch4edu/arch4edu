# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=GPArotation
_pkgver=2024.2-1
pkgname=r-${_pkgname,,}
pkgver=2024.2.1
pkgrel=1
pkgdesc='GPA Factor Rotation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ad34a145da4a259b32035a3a061e93a67e8af27d91893449f77d2ab32bd7482b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

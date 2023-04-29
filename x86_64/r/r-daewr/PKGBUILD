# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=daewr
_pkgver=1.2-10
pkgname=r-${_pkgname,,}
pkgver=1.2.10
pkgrel=1
pkgdesc='Design and Analysis of Experiments with R'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-stringi
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6ea1af5488a9ec719987e742e0e00683b0e2d5051451bcd6947e5211acc49341')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

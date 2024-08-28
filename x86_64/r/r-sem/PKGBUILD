# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=sem
_pkgver=3.1-16
pkgname=r-${_pkgname,,}
pkgver=3.1.16
pkgrel=1
pkgdesc='Structural Equation Models'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-mi
)
optdepends=(
  r-diagrammer
  r-polycor
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a39f3ebf9dd7b08e3142ad1d1fcddfd79f7f260e08255e3d8b960e5ed085c94b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

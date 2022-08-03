# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=2.6
pkgname=r-${_pkgname,,}
pkgver=2.6
pkgrel=4
pkgdesc='One-Way Tests in Independent Groups Designs'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-car
  r-ggplot2
  r-moments
  r-nortest
)
optdepends=(
  r-aid
  r-tibble
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('39a2e7dc107d9b7848d7b9cc27718c56840a254c02505263d4fba65e4c8e0217')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

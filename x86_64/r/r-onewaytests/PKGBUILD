# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=onewaytests
_pkgver=2.7
pkgname=r-${_pkgname,,}
pkgver=2.7
pkgrel=1
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
sha256sums=('cd0e043cfbe6a630bcbb419b6e57c17b1e0fe75fecb482118f72d66c86ca6490')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

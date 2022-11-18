# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.3.19
pkgname=r-${_pkgname,,}
pkgver=2.3.19
pkgrel=1
pkgdesc="Dependencies for the 'jamovi' Framework"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-base64enc
  r-jsonlite
  r-r6
  r-rlang
  r-stringi
)
optdepends=(
  r-fastmap
  r-ggplot2
  r-knitr
  r-ragg
  r-rcolorbrewer
  r-rprotobuf
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('afbd51b229ce3ba004def57a8fcced5e44f6fc2a33305b8c8d5d8362cf878c33')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

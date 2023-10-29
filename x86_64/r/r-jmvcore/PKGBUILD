# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=jmvcore
_pkgver=2.4.7
pkgname=r-${_pkgname,,}
pkgver=2.4.7
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
sha256sums=('6a5c520ea8d94fbd4863415323a5dc6566579a29d7cde4d838cec13973d9ecdf')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

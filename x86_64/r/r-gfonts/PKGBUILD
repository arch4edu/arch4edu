# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gfonts
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=0.2.1
pkgrel=1
pkgdesc="Offline 'Google' Fonts for 'Markdown' and 'Shiny'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-crayon
  r-crul
  r-glue
  r-htmltools
  r-jsonlite
  r-shiny
)
optdepends=(
  r-covr
  r-knitr
  r-rmarkdown
  r-testthat
  r-vcr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b970a877ee5a1b530aa6936309f7d81670ee8caf429c7b778755d8d7e8708dec')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

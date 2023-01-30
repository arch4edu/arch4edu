# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gfonts
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=0.2.0
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
sha256sums=('72e2eead5280b45aadbbd9385971d65e9866fd659270b1c3c1eb98330f024aa6')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

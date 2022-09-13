# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=DT
_pkgver=0.25
pkgname=r-${_pkgname,,}
pkgver=0.25
pkgrel=1
pkgdesc="A Wrapper of the JavaScript Library 'DataTables'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-crosstalk
  r-htmltools
  r-htmlwidgets
  r-jquerylib
  r-jsonlite
  r-magrittr
  r-promises
)
optdepends=(
  r-bslib
  r-knitr
  r-rmarkdown
  r-shiny
  r-testit
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0dfc8713062e1fe4e0428936367f35a0a41616c27b6d9b002bdfda58091c442b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=reactR
_pkgver=0.6.1
pkgname=r-${_pkgname,,}
pkgver=0.6.1
pkgrel=1
pkgdesc='React Helpers'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-htmltools
)
optdepends=(
  r-htmlwidgets
  r-jsonlite
  r-knitr
  r-rmarkdown
  r-shiny
  r-usethis
  r-v8
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9b690d7d4de54cbecca16deea9684f1d4aba91b2b280b38ea13c63eb5e57d892')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

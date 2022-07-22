# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ggpol
_pkgver=0.0.7
pkgname=r-${_pkgname,,}
pkgver=0.0.7
pkgrel=4
pkgdesc="Visualizing Social Science Data with 'ggplot2'"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-dplyr
  r-ggplot2
  r-glue
  r-gtable
  r-plyr
  r-rlang
  r-tibble
)
optdepends=(
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('35684f5be49148e584269d63e5cc34cc46b6c16e9e90ca435952cecaa711b987')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

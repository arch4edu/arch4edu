# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=gginnards
_pkgver=0.2.0
pkgname=r-${_pkgname,,}
pkgver=0.2.0
pkgrel=1
pkgdesc="Explore the Innards of 'ggplot2' Objects"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ggplot2
  r-magrittr
  r-rlang
  r-stringr
  r-tibble
)
optdepends=(
  r-knitr
  r-pryr
  r-rmarkdown
  r-sf
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0f0312fc60a44ed4e3c50d895485f2d63d4b34dc8aec064af7efd1ca26b01676')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

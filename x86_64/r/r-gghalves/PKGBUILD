# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gghalves
_pkgver=0.1.4
pkgname=r-${_pkgname,,}
pkgver=0.1.4
pkgrel=1
pkgdesc='Compose Half-Half Plots Using Your Favourite Geoms'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-ggplot2
  r-gtable
)
optdepends=(
  r-dplyr
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('a73bc8b6b9c23d421708a0732e53494cb864edbf2a917418beec93bfbec05de3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

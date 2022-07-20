# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=threejs
_pkgver=0.3.3
pkgname=r-${_pkgname,,}
pkgver=0.3.3
pkgrel=4
pkgdesc='Interactive 3D Scatter Plots, Networks and Globes'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-base64enc
  r-crosstalk
  r-htmlwidgets
  r-igraph
)
optdepends=(
  r-knitr
  r-maps
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('76c759c8b20fb34f4f7a01cbd1b961296e1f19f4df6dded69aae7f1bca80219c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

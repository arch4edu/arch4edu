# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=patchwork
_pkgver=1.3.2
pkgname=r-${_pkgname,,}
pkgver=1.3.2
pkgrel=2
pkgdesc='The Composer of Plots'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cli
  r-ggplot2
  r-gtable
  r-rlang
)
optdepends=(
  r-covr
  r-gridextra
  r-gridgraphics
  r-knitr
  r-png
  r-ragg
  r-rmarkdown
  r-testthat
  r-vdiffr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0ec469acfd69d1a4f1a6317c861e6bf000f768c2d5047e3aed6713df9afe27eb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=patchwork
_pkgver=1.3.0
pkgname=r-${_pkgname,,}
pkgver=1.3.0
pkgrel=1
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
sha256sums=('77af6ec4a4aacebd9b5ba128d97d2fb10cfc4e4c40aded942d6976bab3e52e16')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

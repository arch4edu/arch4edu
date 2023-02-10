# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Hmisc
_pkgver=4.8-0
pkgname=r-${_pkgname,,}
pkgver=4.8.0
pkgrel=3
pkgdesc='Harrell Miscellaneous'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-base64enc
  r-colorspace
  r-data.table
  r-formula
  r-ggplot2
  r-gridextra
  r-gtable
  r-htmltable
  r-htmltools
  r-latticeextra
  r-viridis
)
optdepends=(
  r-acepack
  r-chron
  r-knitr
  r-mice
  r-plotly
  r-plyr
  r-rlang
  r-rms
  r-rstudioapi
  r-tables
  r-vgam
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6392ed4b96c8ea95da1ebfa92b38cc3baa0314babb2680a08800d0b25c0a9b1d')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Hmisc
_pkgver=5.0-1
pkgname=r-${_pkgname,,}
pkgver=5.0.1
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
  r-knitr
  r-rmarkdown
  r-viridis
)
optdepends=(
  r-abind
  r-acepack
  r-chron
  r-digest
  r-kableextra
  r-lattice
  r-latticeextra
  r-leaps
  r-mice
  r-parallel
  r-pcapp
  r-plotly
  r-plyr
  r-polspline
  r-qreport
  r-rio
  r-rlang
  r-rms
  r-rstudioapi
  r-survival
  r-tables
  r-vgam
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('db390f8f8a150cb5cffb812e9609a8e8632ceae0dc198528f190fd670ba8fa59')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

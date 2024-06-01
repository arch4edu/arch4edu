# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Hmisc
_pkgver=5.1-3
pkgname=r-${_pkgname,,}
pkgver=5.1.3
pkgrel=1
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
  r-getpass
  r-gt
  r-htmlwidgets
  r-jsonlite
  r-kableextra
  r-keyring
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
  r-qs
  r-rio
  r-rlang
  r-rms
  r-rstudioapi
  r-safer
  r-sparkline
  r-survival
  r-tables
  r-vgam
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('3c61772ff7a78ca5855189faa810c74117dc5df240103adc6e90eb94e9c605eb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

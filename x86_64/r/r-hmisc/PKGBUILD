# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Hmisc
_pkgver=4.7-0
pkgname=r-${_pkgname,,}
pkgver=4.7.0
pkgrel=5
pkgdesc='Harrell Miscellaneous'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-base64enc
  r-data.table
  r-formula
  r-ggplot2
  r-gridextra
  r-gtable
  r-htmltable
  r-htmltools
  r-latticeextra
  r-viridis
  r-stringi
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
  r-tables
  r-vgam
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('29ec2d9ca11c790c350e93323126bef4f498c69c41c31bb335fd04671e0f87bd')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

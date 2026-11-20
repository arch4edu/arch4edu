# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=vcdExtra
_pkgver=0.9.9
pkgname=r-${_pkgname,,}
pkgver=0.9.9
pkgrel=1
pkgdesc="'vcd' Extensions and Additions"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ca
  r-dplyr
  r-forcats
  r-ggplot2
  r-glue
  r-gnm
  r-gt
  r-here
  r-purrr
  r-readxl
  r-rgl
  r-scales
  r-stringr
  r-tidyr
  r-vcd
  r-igraph
  r-webshot2
)
optdepends=(
  r-aer
  r-car
  r-coin
  r-effects
  r-fahrmeir
  r-gmodels
  r-hmisc
  r-knitr
  r-lattice
  r-lmtest
  r-nnet
  r-plyr
  r-rgl
  r-rmarkdown
  r-seriation
  r-sleuth2
  r-stats4
  r-vgam
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b87ed7eed3b3c923142246f1f64f8dc4f6b89ab13afa46c64aee540ec5894624')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=vcdExtra
_pkgver=0.8-0
pkgname=r-${_pkgname,,}
pkgver=0.8.0
pkgrel=4
pkgdesc="'vcd' Extensions and Additions"
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-ca
  r-gnm
  r-vcd
)
optdepends=(
  r-aer
  r-car
  r-coin
  r-effects
  r-fahrmeir
  r-ggplot2
  r-gmodels
  r-hmisc
  r-knitr
  r-lattice
  r-lmtest
  r-nnet
  r-plyr
  r-rgl
  r-rmarkdown
  r-sleuth2
  r-stats4
  r-vgam
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('b36a69e795c9dfa599bdcb5141518a93cc29efc3d77178a94cc3f0dde4f561f3')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

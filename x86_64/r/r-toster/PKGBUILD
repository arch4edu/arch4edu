# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=TOSTER
_pkgver=0.8.1
pkgname=r-${_pkgname,,}
pkgver=0.8.1
pkgrel=1
pkgdesc='Two One-Sided Tests (TOST) Equivalence Testing'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-cowplot
  r-distributional
  r-ggdist
  r-ggplot2
  r-jmvcore
  r-lifecycle
  r-r6
  r-tidyr
)
optdepends=(
  r-afex
  r-broom
  r-car
  r-knitr
  r-rmarkdown
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('6d540c5c1c773b4556a57e08dc13876772405fcdd829901985b02e5194d23c13')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

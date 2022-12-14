# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=TOSTER
_pkgver=0.6.0
pkgname=r-${_pkgname,,}
pkgver=0.6.0
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
  r-tidyr
)
optdepends=(
  r-afex
  r-broom
  r-car
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ad4aeccec5d0a478de48009ef952edee41843515782023daadff5916f6fa75ed')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

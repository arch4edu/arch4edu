# system requirements: GNU make, C++11
# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=prophet
_pkgver=1.0
pkgname=r-${_pkgname,,}
pkgver=1.0
pkgrel=4
pkgdesc='Automatic Forecasting Procedure'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-bh
  r-dplyr
  r-dygraphs
  r-extradistr
  r-ggplot2
  r-lubridate
  r-rcpp
  r-rcppeigen
  r-rcppparallel
  r-rlang
  r-rstan
  r-rstantools
  r-scales
  r-stanheaders
  r-tidyr
  r-xts
)
optdepends=(
  r-knitr
  r-readr
  r-rmarkdown
  r-testthat
)
makedepends=('make' 'gcc')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('94bea364c7c625bd34fee08da221b7a6c4d3ef939869f22229b2273fb7f2b91a')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

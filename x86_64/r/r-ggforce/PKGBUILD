# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggforce
_pkgver=0.5.0
pkgname=r-${_pkgname,,}
pkgver=0.5.0
pkgrel=1
pkgdesc="Accelerating 'ggplot2'"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('MIT')
depends=(
  r
  r-cli
  r-ggplot2
  r-gtable
  r-lifecycle
  r-polyclip
  r-rcpp
  r-rcppeigen
  r-rlang
  r-scales
  r-systemfonts
  r-tidyselect
  r-tweenr
  r-vctrs
  r-withr
)
makedepends=(
  r-cpp11
)
optdepends=(
  r-concaveman
  r-covr
  r-deldir
  r-latex2exp
  r-reshape2
  r-sessioninfo
  r-units
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('41b3ea33dc4da774a0047a446676e7c4d6c41592ad9cdb21db8d4efebcfb5d53')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

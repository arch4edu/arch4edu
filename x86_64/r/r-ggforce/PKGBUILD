# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ggforce
_pkgver=0.4.2
pkgname=r-${_pkgname,,}
pkgver=0.4.2
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
sha256sums=('c145b0e6ed6847d409ed2fe103b81234855bc0661cde2bfb4410fb23680e51a8')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
  install -Dm644 "${_pkgname}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:

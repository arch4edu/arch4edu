# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bbmle
_pkgver=1.0.25
pkgname=r-${_pkgname,,}
pkgver=1.0.25
pkgrel=1
pkgdesc='Tools for General Maximum Likelihood Estimation'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-bdsmatrix
  r-mvtnorm
  r-numderiv
)
optdepends=(
  r-aiccmodavg
  r-emdbook
  r-ggplot2
  r-hmisc
  r-knitr
  r-mumin
  r-optimx
  r-rms
  r-runit
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('86a8c69902fbf6caf337f9bc532afe89dc2a59dd24287a2423d781797010b255')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bbmle
_pkgver=1.0.25.1
pkgname=r-${_pkgname,,}
pkgver=1.0.25.1
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
sha256sums=('d92a0cf819fe4c08b8eb17f5e03275c8accde7f3b54f990cbba5ab926575b60b')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

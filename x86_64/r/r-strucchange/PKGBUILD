# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=strucchange
_pkgver=1.5-3
pkgname=r-${_pkgname,,}
pkgver=1.5.3
pkgrel=1
pkgdesc='Testing, Monitoring, and Dating Structural Changes'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-sandwich
  r-zoo
)
optdepends=(
  r-car
  r-dynlm
  r-e1071
  r-foreach
  r-lmtest
  r-mvtnorm
  r-stats4
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('cac6b4028f68cc8d39202377161d0f7f72ea229b552a5c35769053ab89f90f86')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

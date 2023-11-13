# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ranger
_pkgver=0.16.0
pkgname=r-${_pkgname,,}
pkgver=0.16.0
pkgrel=1
pkgdesc='A Fast Implementation of Random Forests'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
  r-rcppeigen
)
optdepends=(
  r-survival
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('0395f93afdb807a7882c1fa8f183a26a871c5168ea0903566951298ef1138589')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

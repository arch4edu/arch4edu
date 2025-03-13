# system requirements: A C++11 compiler; g++ (>= 4.9.*) or newer works.
# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=RcppTOML
_pkgver=0.2.3
pkgname=r-${_pkgname,,}
pkgver=0.2.3
pkgrel=1
pkgdesc="'Rcpp' Bindings to Parser for Tom's Obvious Markup Language"
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-rcpp
)
optdepends=(
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('2ed594253c562bef7065e67d791197f61b221e545206a1b3598d46868cf5926f')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

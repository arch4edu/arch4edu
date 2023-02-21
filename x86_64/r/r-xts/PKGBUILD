# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xts
_pkgver=0.13.0
pkgname=r-${_pkgname,,}
pkgver=0.13.0
pkgrel=1
pkgdesc='eXtensible Time Series'
arch=('x86_64')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-zoo
)
optdepends=(
  r-chron
  r-runit
  r-timedate
  r-timeseries
  r-tis
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('188e4d1d8c3ec56a544dfb9da002e8aac80b9303d0a5a1f62ff0e960aeef9674')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

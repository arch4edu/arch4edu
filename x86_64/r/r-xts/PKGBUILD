# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=xts
_pkgver=0.13.2
pkgname=r-${_pkgname,,}
pkgver=0.13.2
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
  r-timedate
  r-timeseries
  r-tinytest
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4ad590f65c4c9daa7fe920aee0274a23478daacbfcd6edc2566dc392460f1dfb')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

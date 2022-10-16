# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xts
_pkgver=0.12.2
pkgname=r-${_pkgname,,}
pkgver=0.12.2
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
  r-fts
  r-runit
  r-timedate
  r-timeseries
  r-tis
  r-tseries
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('9c287ceaeb758ff4c9596be6a688db5683d50b45e7610e6d068891ca10dca743')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

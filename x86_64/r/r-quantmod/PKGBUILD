# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=quantmod
_pkgver=0.4.21
pkgname=r-${_pkgname,,}
pkgver=0.4.21
pkgrel=1
pkgdesc='Quantitative Financial Modelling Framework'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-curl
  r-ttr
  r-xts
  r-zoo
)
optdepends=(
  r-dbi
  r-downloader
  r-jsonlite
  r-rmysql
  r-rsqlite
  r-timeseries
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('4e06d06712da011bb7fc26c44ff95bf612fa23e1594b02877938561dd26cb7e2')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

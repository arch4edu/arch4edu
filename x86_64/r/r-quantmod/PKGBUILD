# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=quantmod
_pkgver=0.4.29
pkgname=r-${_pkgname,,}
pkgver=0.4.29
pkgrel=1
pkgdesc='Quantitative Financial Modelling Framework'
arch=('any')
url="https://cran.r-project.org/package=${_pkgname}"
license=('GPL')
depends=(
  r
  r-curl
  r-jsonlite
  r-ttr
  r-xts
  r-zoo
)
optdepends=(
  r-dbi
  r-downloader
  r-rmysql
  r-rsqlite
  r-timeseries
  r-xml2
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
sha256sums=('ed2a56c96cd3acdb2f4fa27ac9f7177dfb40adaad125bba819c2b26cff636c71')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

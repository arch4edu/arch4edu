# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=quantmod
_pkgver=0.4.27
pkgname=r-${_pkgname,,}
pkgver=0.4.27
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
sha256sums=('71d3c02b61c22eb1ab2c3b17ad9e493b601af97dd47c43c2263914c964620141')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

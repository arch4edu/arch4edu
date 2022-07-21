# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=xts
_pkgver=0.12.1
pkgname=r-${_pkgname,,}
pkgver=0.12.1
pkgrel=4
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
sha256sums=('d680584af946fc30be0b2046e838cff7b3a65e00df1eadba325ca5e96f3dca2c')

build() {
  R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
# vim:set ts=2 sw=2 et:

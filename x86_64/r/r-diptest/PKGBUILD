# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=diptest
_pkgver=0.77-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hartigan's Dip Test Statistic for Unimodality - Corrected"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('18b630a2c9c1987954031271aadbd97c')
b2sums=('9dc6461c98d6d7571e5db1dde9946c51a227a6cf3ee853cfd97423d4ae0445d372635e42de515184cb9eacb3e0880f91aba59278354809c9d1d507833ba93f00')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Phil Schaf <flying-sheep@web.de>

_pkgname=corpcor
_pkgver=1.6.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Efficient Estimation of Covariance and (Partial) Correlation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e048dc1fb5bb9ffee6d22a3ea24fe673')
b2sums=('8a19ab06ebf82ecb8fcff638a95bf92746e6143a1497fe35b50675c7e3fbe636e6bc3ed297c39020be4317c105c7f7dc922806a57702a672694bf7eac0d1143b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

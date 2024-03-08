# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=goftest
_pkgver=1.2-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="Classical Goodness-of-Fit Tests for Univariate Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a0b5ead2181094d4a929708f700a4bdc')
b2sums=('a1b0ae4ff1e930ca59a03c81a605169daafc29dcf5dd31f6392e2be9d0f7178027827c7bdc93f31497e2f3224368b4364bcbb88d93afb86ff8faf12981e91cdb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

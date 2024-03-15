# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=evd
_pkgver=2.3-6.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Functions for Extreme Value Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-interp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('01db8aaa75099d3afb844c0378ce49d0')
b2sums=('384a900123ad6647c7a79d517c8c6ac2d805823c1bfc5c1a927ff46a310bbd0b9ac998605bf8d61427cd7523735c425d6f8eafa880078347b2e204bc2d88c200')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

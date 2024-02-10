# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=numbers
_pkgver=0.8-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Number-Theoretic Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-gmp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('3f9d482326ca6c5360df4f49c0849c2f')
b2sums=('8554d6f469f2a97ce250d46c131d15a986eee77c43878f4c8f3235b81a0b65118c0fdfbfe664e3614e415c0ef651e7f509eec757ce6dd9aa9f5bc9eda764ddd6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

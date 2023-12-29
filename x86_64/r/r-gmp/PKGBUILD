# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmp
_pkgver=0.7-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Multiple Precision Arithmetic"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  gmp
  r
)
optdepends=(
  r-rmpfr
  r-round
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a5d59ee060a3b2f83f01df8ee48343c5')
b2sums=('6f4affd57c1537a72c1680865c806fbf1014b1efbb751025a19d39602b4b09382d08958b0a942a662815c021d580849297364b9bfbcc9784c8577271dc5595e0')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

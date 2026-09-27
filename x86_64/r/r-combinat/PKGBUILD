# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=combinat
_pkgver=0.0-9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Combinatorics Utilities"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0ddb3b2f0588a34003f05aa46faef1d2')
b2sums=('7102fa4d85d6e1753260d9360ded8624b31b51f48b616fb793ffc4341de522422a4e70586900121b8152b51c05422efed805bc72475604e7f20aa6929fadc47c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

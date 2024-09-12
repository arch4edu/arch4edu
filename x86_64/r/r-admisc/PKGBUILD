# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=admisc
_pkgver=0.36
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adrian Dusa's Miscellaneous"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-qca
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1bd6539d9d5ce429884d5ef949d39a06')
b2sums=('749bce40ffeb91ab64daa686985fdf807d156deacb086b59136be7b62aecc5ac98246ff76d5be673e74b1188bc290567920d350d39763dac679ed8fe7ccd3fb4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pixmap
_pkgver=0.4-14
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bitmap Images / Pixel Maps"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('257d33ea7e5740e24f466ccee7860c3e')
b2sums=('a993e445b3269328a27734d62e081504627f5be49ff356b8fd04a05eac5225c5766f2d465b1dfea33e8b91df299e2782b89a23b4508033a59379ab69801daefe')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

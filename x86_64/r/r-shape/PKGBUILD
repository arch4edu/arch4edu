# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=shape
_pkgver=1.4.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Functions for Plotting Graphical Shapes, Colors"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL3)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('41827d1eed10cfb32f3cf2d75817ba18')
b2sums=('d0bee95680affa418254700e9a89df9e31ee4f96e4bf3a9915fd878b17f184e57c010844c150041556a4894392e94b0a191fb02bfb342f7a88257e1eda61b126')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

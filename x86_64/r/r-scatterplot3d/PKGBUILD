# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=scatterplot3d
_pkgver=0.3-44
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="3D Scatter Plot"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0acaab2e9eba4ece27e1444f769d006b')
b2sums=('b5b09fecaa0a42738b83574a6e9941c11d03a0051f07c4c20ae89b1a4f54bf18d585364a03d8fe8f5cb3cb686f5850272b7a2366bf325c9beb84595bb7189a46')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

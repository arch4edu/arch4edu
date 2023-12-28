# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=combinat
_pkgver=0.0-8
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=9
pkgdesc="combinatorics utilities"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8fb5132227894e7e5e01d8183395a7ac')
b2sums=('7fcfb38c482be4dec2a10ef05a508fb13ae5f5e17066d65c3b3318f5268a6a718c9bd406f5dcc2dbf4d2d4b7af7ea53a8072422b79b9355d795f39c3ba9a0e02')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

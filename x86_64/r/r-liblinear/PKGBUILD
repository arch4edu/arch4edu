# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LiblineaR
_pkgver=2.10-24
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Predictive Models Based on the LIBLINEAR C/C++ Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-sparsem
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4060a16fd9f48162af18a17469192561')
b2sums=('d01ec8007681afe70f2dac6919d085c3c4c3174fcc0f0aa99bd5658c802c1536b733bf720e56b742b210b58b7b55dfcc2b7012541220b6f4cbca191dcff127fd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=gmp
_pkgver=0.7-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('9d8e130ae524e48d0f62d7db0ac379ed')
b2sums=('e55437c870b138830168a69ddfe27e9f97aa62a3a954c3ceab637edcff42a817d543f5ad4d579f727d0a764763fe76e83bb98d148e4b7619671850fa6f6ed614')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

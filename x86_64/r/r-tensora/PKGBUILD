# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=tensorA
_pkgver=0.36.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Advanced Tensor Arithmetic with Named Indices"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('262cae742a4518d5e16fd13aa45158cc')
b2sums=('df87d0fc1fdd22ce56c806b4ff2aaad9e95930b19c28e3711bbc621e513e0b81ccf49c97b052e512db515e5db2a99d22c9e07e1ece05c3c8575e988c4437053e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

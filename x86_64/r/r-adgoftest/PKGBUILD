# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=ADGofTest
_pkgver=0.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Anderson-Darling GoF test"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a601ed539181dce143fcbc738f75fa7b')
b2sums=('bbc5d3963aa2bb06bbdeb25f4273a7de5d9a0569e1638c5abb8246395a3a9d180de4a4351527a64b641ccc59fbdaac16c65ea6cb5980b609238cee1e58212d07')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

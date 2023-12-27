# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=permute
_pkgver=0.9-7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=12
pkgdesc="Functions for Generating Restricted Permutations of Data"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(GPL2)
depends=(
  r
)
optdepends=(
  r-bookdown
  r-knitr
  r-rmarkdown
  r-sessioninfo
  r-testthat
  r-vegan
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('59ea7f860beed70245fe14ebdee3cb1e')
b2sums=('fed45d7e5fef621a64cd7f0de708c6c3e4e684ebc81cbe68bde161294ca5a56ff29450025de2666835caab1381cee1b728c0aa01cd88ddfc0c8500b4ff454fa2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

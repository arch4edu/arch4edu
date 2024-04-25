# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=numDeriv
_pkgver=2016.8-1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=14
pkgdesc="Accurate Numerical Derivatives"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f894081f6d73822a362f156e849c9657')
b2sums=('33bf377a66146eeff74795930ff32d7db73d19b4e9c6a147d3222e8d1cebae39751ae457c49a6da23b4040532f3bb077788a4ae6d22b1ffb7b66a26487e70c00')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

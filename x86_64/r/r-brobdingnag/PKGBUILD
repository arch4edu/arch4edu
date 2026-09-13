# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Brobdingnag
_pkgver=1.3-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Very Large Numbers in R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-cubature
  r-knitr
  r-markdown
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a7d48d668c8ee345edd346f0cee40658')
b2sums=('e1fd4805e56939e7b2bbbcdf914390aee407d6c1bd6233325b132afae73861ac569cb785ba1f36a8f16580185cff3a32acf5d4dc48a45353dde654da27f8e186')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

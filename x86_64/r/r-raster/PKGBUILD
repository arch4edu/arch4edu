# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Jooa <aur at (name) dot xyz>

_pkgname=raster
_pkgver=3.6-32
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Geographic Data Analysis and Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-rcpp
  r-sp
  r-terra
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-exactextractr
  r-fields
  r-gstat
  r-igraph
  r-ncdf4
  r-rastervis
  r-sf
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('83f16331a25805fdcccabee2b97f4bca')
b2sums=('85e5a2d6c9858d262234486dfa09df1908dfde7b7b384c029632417d3ee7703e41d8a4b085a5b39b945950e36926c3f871b6d0617ab60d675265fa24d7cea51b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

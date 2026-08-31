# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=terra
_pkgver=1.9-46
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Spatial Data Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r-rcpp
  gdal
  geos
  proj
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-deldir
  r-future
  r-future.apply
  r-htmlwidgets
  r-igraph
  r-leaflet
  r-ncdf4
  r-sf
  r-tinytest
  r-xml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7a3e7cfb2eb2184bae8eb2318b5f7908')
b2sums=('d0f61100e0d2777c8dcc6f99e39c4f7d808831513b793ef72f2ae4382f9cca1a4a1a5195d9469daed7b7f51d0577fb5986c5bcb0737578483568df2f0c71895b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

_check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

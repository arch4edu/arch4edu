# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=terra
_pkgver=1.9-60
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
md5sums=('7201ba70b47c49a1ddb189c57aad8339')
b2sums=('2bb5e829a5f8b505120f93b660f1c605bf1ac20094e81f85dce1a9eb6c8da8234e53ca642fde743bc423e7ea70fe576cc96d7d82e0f7bcc56a0834279c99a03e')

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

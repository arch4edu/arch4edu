# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=iBreakDown
_pkgver=2.1.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Model Agnostic Instance Level Variable Attributions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-ggplot2
)
optdepends=(
  r-covr
  r-dalex
  r-e1071
  r-jsonlite
  r-knitr
  r-r2d3
  r-randomforest
  r-ranger
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1db5e84db005e7daf9474ea073b23789')
b2sums=('a4c6592563e2219f4c12c50592733638e1436b65e56fa8dee6cf2075b4e2c367700b16d5b128370413e227594c5cfa6bbd99ccc635bebbc982e2feca5819c4e7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ingredients
_pkgver=2.3.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Effects and Importances of Model Ingredients"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-ggplot2
  r-gridextra
  r-scales
)
optdepends=(
  r-covr
  r-dalex
  r-gower
  r-jsonlite
  r-knitr
  r-r2d3
  r-ranger
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('46458d9e09b13c884e88f8ebfdcd5a29')
b2sums=('d771328f64a1ed4460ee21913633a56fee89e253f88fbc185937dc243b610b4c8b37fed57bd4104da94cecefd8593126758fa44c78e21f0ded4d04ba6dcb0cd4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

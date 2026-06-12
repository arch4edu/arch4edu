# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.6-50
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Restricted Statistical Estimation and Inference for Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-future
  r-future.apply
  r-ggplot2
  r-gridextra
  r-lavaan
  r-mvtnorm
  r-norm
  r-progressr
  r-quadprog
  r-scales
  r-tmvtnorm
)
optdepends=(
  r-bain
  r-knitr
  r-metadat
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('1589e8eda58d4c42c9120b4e5e9f64c0')
b2sums=('428a26c794a3aa0f2ca9516159efe4bf8603b3264ce2b9df54e16aaba3dabbe1a20649bc2cde90c3fb8d7c814c568a0a8426768027f8d43b9c9ae957a175ceb7')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

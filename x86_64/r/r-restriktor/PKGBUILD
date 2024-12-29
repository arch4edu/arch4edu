# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.6-10
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
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a24820deb75a3fc155709d54bd0ced81')
b2sums=('a9fe3407a97b11c93696e6c550984eb343a31abcfd448d2d818f00d230243cf31b8226b38339e9f52a1ffd9f5dfde03f8487751ceea2c44c43cb10b6bdc977d9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

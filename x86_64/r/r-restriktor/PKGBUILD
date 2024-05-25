# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-60
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Restricted Statistical Estimation and Inference for Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-ggplot2
  r-glue
  r-ic.infer
  r-lavaan
  r-mvtnorm
  r-norm
  r-pbapply
  r-quadprog
  r-tmvtnorm
)
optdepends=(
  r-bain
  r-knitr
  r-rmarkdown
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('9e62e5f2e9b11712c9baf8d37bead2c5')
b2sums=('5c6f084082e27ab518584d7769c85147278e10d3be1e977cc9f29ff31d7badf9841e3e609c0b44fb6bf4cac001a9a9c2252c825b2043eedf97ba8bfd6d9b1038')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

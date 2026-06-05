# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.6-30
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
md5sums=('35ccecb57bebcb751424532baaeab3af')
b2sums=('49099a791fd1b0e7497d3dd000fe1d65d7a9144cc97f3fb4ff3ed905c3d8850530c23958ca560ddc914cbd7fd447a5e11c5d409796139ccfc77721c664d41420')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

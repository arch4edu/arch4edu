# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-30
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Restricted Statistical Estimation and Inference for Linear Models"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-ggplot2
  r-ic.infer
  r-lavaan
  r-mvtnorm
  r-norm
  r-quadprog
)
optdepends=(
  r-bain
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ec3023fa71654bd421e7c1f82c1be9fc')
sha256sums=('2f91995e1248280a4068017fa418431211a480a8add0166915248a9e45428be2')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

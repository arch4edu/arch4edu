# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: sukanka <su975853527@gmail.com>

_pkgname=restriktor
_pkgver=0.5-90
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('421b35b95ef5549ed952143db5036846')
b2sums=('b3cadbd8d1ce4d6a043d630bea2491ce2227f20060993ed28f008ac0af0f4efe936d83687b3fc43ce6e59ba7312b3ab0e84557855cb2076884d853a3b86da041')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

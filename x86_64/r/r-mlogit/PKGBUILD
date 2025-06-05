# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mlogit
_pkgver=1.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multinomial Logit Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-dfidx
  r-formula
  r-lmtest
  r-rdpack
  r-statmod
  r-zoo
)
optdepends=(
  r-aer
  r-car
  r-ggplot2
  r-knitr
  r-rmarkdown
  r-texreg
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e06d5b839e89c43e4a316c0efe1b458e')
b2sums=('0d0c95288d99359a6910326095284482048ca4ad2d28c5375b643afaefc5053a9f6705bf9e478743bd925eb0056de96ea00ca3acb835c9bcbea6235e641386ce')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

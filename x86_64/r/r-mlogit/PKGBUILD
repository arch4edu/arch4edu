# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=mlogit
_pkgver=1.1-3
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
md5sums=('7730ed9af843f513212338c062adae30')
b2sums=('1f9ac927b4fc16b35f3f86e0ebf58ff700e66ebf9d7cf02aa0cca1f4aa9d4a6cb8027baadfddc91eb9f245da19379aa1126cd63f6cfaef598def8e97568b80e9')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

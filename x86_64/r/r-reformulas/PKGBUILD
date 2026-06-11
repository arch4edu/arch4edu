# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=reformulas
_pkgver=0.4.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Machinery for Processing Random Effect Formulas"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-rdpack
)
optdepends=(
  r-lme4
  r-formula
  r-tinytest
  r-glmmtmb
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('280fedda4433e3ec798cb36103f75b92')
b2sums=('c5f80fcf2f08e2e0e8f53e4a5e8bccd2ef64c43c5b65219628db4ad802c856a8bfbefabf4728ed61f7dd56d4ea052354a83b2138b0b4d2046d14747dea756f37')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

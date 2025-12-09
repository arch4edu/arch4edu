# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=dfidx
_pkgver=0.2-0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Indexed Data Frames"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-formula
  r-rdpack
)
optdepends=(
  r-knitr
  r-quarto
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('735200d5d2bda6489b28b96dfbd4617d')
b2sums=('50ad10ee8be24bf71040cbb10e9c96be39477797d8a3c420ce9ae57b831ccbdbb5bc4fdffaa57bc43da3c191995fe27c218986dea5a3297f0ab709367ed1d2b1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

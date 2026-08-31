# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=QuickJSR
_pkgver=1.11.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Interface for the 'QuickJS-NG' Lightweight 'JavaScript' Engine"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r
)
checkdepends=(
  r-tinytest
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4eb9c9ec59be0b2bdf113969781f61ac')
b2sums=('3f7d3beb8e7fef81c4406fc0047115c31d1f98c600fb3c734441d8e1001de5f9200a5ae06f55e1e724d0519c330d97d202a18347a0c8832856e9510f882f22d2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}

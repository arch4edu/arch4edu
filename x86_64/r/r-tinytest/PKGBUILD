# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=tinytest
_pkgver=1.4.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=2
pkgdesc="Lightweight and Feature Complete Unit Testing Framework"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e8d57668032bedd980cc9f1ad9c957d3')
sha256sums=('f6fc13887d096ba444fb722ef34cc88e079fc18be9668ffead1ba586a30b1c74')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla tinytest.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

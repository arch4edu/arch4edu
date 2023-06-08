# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RUnit
_pkgver=0.4.32
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=10
pkgdesc="R Unit Test Framework"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
depends=(
  r
)
optdepends=(
  r-xml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5e72a1820cfc8e68e8bc04cb27664196')
sha256sums=('23a393059989000734898685d0d5509ece219879713eb09083f7707f167f81f1')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=jomo
_pkgver=2.7-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="Multilevel Joint Modelling Multiple Imputation"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL2)
depends=(
  r-lme4
  r-ordinal
  r-tibble
)
optdepends=(
  r-mitml
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('473d277969676494a6df604b477809e9')
sha256sums=('3ffa2a5521d4969fe77b23cd3ab201afdf8db3f8f708b1276c33083c01d7e2da')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

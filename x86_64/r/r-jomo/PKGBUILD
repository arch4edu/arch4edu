# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=jomo
_pkgver=2.7-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Multilevel Joint Modelling Multiple Imputation"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
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
b2sums=('b0b4f6ec30a0178fc484ee71c052ec21606308e13bf9db5240917d004d3e212e41ff9656ea0124e2ebf4203e7808959c05c9fe6af078cf5ae065823cc22d820e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

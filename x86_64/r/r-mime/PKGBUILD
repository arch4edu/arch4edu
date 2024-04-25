# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Kibouo <csonka.mihaly@hotmail.com>
# Contributor: Alex Branham <alex.branham@gmail.com>

_pkgname=mime
_pkgver=0.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=14
pkgdesc="Map Filenames to MIME Types"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7314f3b57f70474d9b4d2b831d6bb59d')
b2sums=('62f88bc0f414216f062d93541f20ef650756a51ec88e27a29ecf1e4418182a5bedf855cbfd77dc63497f15a0e2a64c8b07d81eb91c4ef2f74e74a2c54ca4926f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla mime.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

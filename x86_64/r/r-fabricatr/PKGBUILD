# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fabricatr
_pkgver=1.0.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Imagine Your Data Before You Collect It"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-rlang
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-data.table
  r-extradistr
  r-mvnfast
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d0e4c325160f22c0b8697a66906b35ea')
b2sums=('8a48540da7b0fcf167263436cfa3ed7681b6a83a82eed2a583224d63f78603ecbd5fe9b97032eb5c05808fa0bd3b942117e73942e6ac719b8c515c045b2bed85')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}

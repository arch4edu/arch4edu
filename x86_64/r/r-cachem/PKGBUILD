# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=cachem
_cranver=1.0.8
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Cache R Objects with Automatic Pruning"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(r-rlang r-fastmap)
checkdepends=(r-testthat)
optdepends=(r-testthat)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('ea9ca919fe615dce8770758ecc2fc88ac99074f66ff1cde3a0b95d40007f45c2')

build() {
  mkdir -p build
  R CMD INSTALL "$_cranname" -l build
}

check() {
  cd "$_cranname/tests"
  R_LIBS="$srcdir/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_cranname" "$pkgdir/usr/lib/R/library"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/R/library/$_cranname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}

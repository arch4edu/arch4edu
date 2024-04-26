# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=modelenv
_pkgver=0.1.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Provide Tools to Register Models for Use in 'tidymodels'"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  r-glue
  r-rlang
  r-tibble
  r-vctrs
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz"
        "$_pkgname-fix-tests.patch::https://github.com/tidymodels/modelenv/commit/10584477d8f6a1161f6460c712141e5e533b6d15.patch")
md5sums=('3ea3e9365c8c36752036b20aec780a6f'
         'f820cdd6d2115f0cdd2b25c81a34dc89')
b2sums=('c7031c9fc89c04cc0e1b018ee76cad4fdd0827d0724010f818a4a2a670b32e3c24a68d3f69ef9979d4ea83d3eb1305fb725ab73cb9e468a53322f2dff0ae8c71'
        'b38322a81486908d8c19e6654edb9e5f716c071d21b1f06f49ed3c576f7324823782e68fefe453fa4cd4edc4cd6675b2d7aa6c08ea2c32e5e14088267ce66462')

prepare() {
  # fix outdated snapshot tests
  patch -Np1 -d "$_pkgname" < "$_pkgname-fix-tests.patch"
}

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

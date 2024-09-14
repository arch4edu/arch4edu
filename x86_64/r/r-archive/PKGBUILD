# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=archive
_pkgver=1.1.9
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multi-Format Archive and Compression Support"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('MIT')
depends=(
  libarchive
  r-cli
  r-glue
  r-rlang
  r-tibble
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8b3495e71219952809cd1412d3ea8420')
b2sums=('1878144e23c3fdeca951b616d41be9e80889773cde38b56dbfbdf07d235bb83f0b642a452be145c58d960463fb1fd39429f5e8c50cbf6f1295baf1f7646954b2')

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

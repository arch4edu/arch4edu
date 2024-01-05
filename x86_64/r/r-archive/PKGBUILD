# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=archive
_pkgver=1.1.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Multi-Format Archive and Compression Support"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(MIT)
depends=(
  libarchive
  r-cli
  r-glue
  r-rlang
  r-tibble
)
makedepends=(
  r-cpp11
)
checkdepends=(
  r-testthat
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f3504e5b4704312ce00d704d1e186083')
sha256sums=('11efd69302d4fbc940b740451a4284cdc348e3401ae70d2de37612130ee07d7c')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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

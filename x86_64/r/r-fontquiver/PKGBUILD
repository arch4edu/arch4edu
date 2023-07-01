# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontquiver
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Set of Installed Fonts"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL3)
depends=(
  r-fontbitstreamvera
  r-fontliberation
)
checkdepends=(
  r-htmltools
  r-testthat
)
optdepends=(
  r-htmltools
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('eddbde07ef14475acfbdc9e82d45385a')
sha256sums=('95871814c2d55c03ee15a54e29aadfb840c791e1430f94127d9e1dc8608a6363')

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
}

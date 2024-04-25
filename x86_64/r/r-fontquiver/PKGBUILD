# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=fontquiver
_pkgver=0.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="Set of Installed Fonts"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
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
b2sums=('5cf4b9c82b574be02b7f0b5e9b6c7f1bc9d7defc713d1b0a3a45d352cfff5340678751e78505157c28f69585aaceb3674a9cd237e44649c53f461b4f401d21f4')

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
}

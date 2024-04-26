# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RcppProgress
_pkgver=0.4.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="An Interruptible Progress Bar with OpenMP Support for C++ in R Packages"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
checkdepends=(
  r-devtools
  r-rcpparmadillo
  r-testthat
)
optdepends=(
  r-devtools
  r-rcpparmadillo
  r-roxygen2
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('29ecb32d5c739805ced912e4bedf26f2')
b2sums=('660dfd820fd4d2f32957c8540f4169ecd4736549092d5e0cf4e7f70b0e1661361ee7f710f5a0d3a8479715580915b815a959d06a20fcb55e2e6bfea37fda1c56')

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

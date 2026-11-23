# Maintainer: Adityarup Laha <me@adityaruplaha.me>

_pkgname=micsr
_pkgver=0.1-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="Microeconometrics with R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-compquadform
  r-dfidx
  r-formula
  r-generics
  r-numderiv
  r-rcpp
  r-rdpack
  r-sandwich
)
optdepends=(
  r-aer
  r-censreg
  r-ggplot2
  r-lmtest
  r-mlogit
  r-modelsummary
  r-quarto
  r-sampleselection
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('90542ab8462340d1bb52c82ba0d7f98d')
b2sums=('3a4ef97b07e3547af7c46f99a3b404672753eb765fabebc4df57d0337481e741a1e6bd015c7f40bfefd1b6a685df7c2d5c0b19b8871e61eb825e33dfc33c1ccc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=Boom
_pkgver=0.9.15
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Bayesian Object Oriented Modeling"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-only')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4a0c497336570708c98b611676359249')
b2sums=('4bd6fd2b838dd36b2b11def25192e1ce01d64c91494436d6fddd58c1c25ed8a61d54197c5909838320d9d0542f1e02d732d10d8b611cae3eeeacee06b23f452f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

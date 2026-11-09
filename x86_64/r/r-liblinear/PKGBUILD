# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=LiblineaR
_pkgver=2.50-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Predictive Models Based on the LIBLINEAR C/C++ Library"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-knitr
  r-rmarkdown
  r-sparsem
  r-spelling
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('065aee428c08336d9c62f693ac8094a6')
b2sums=('5bc996eaa87d207bb7902292dba779da013e631cd91ca5acad74486fb57ed0815651b6cc46a7cc72019517e74f96cfa0362a708f2d3634350038bd0d20383205')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

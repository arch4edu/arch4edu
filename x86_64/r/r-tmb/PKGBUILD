# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=TMB
_pkgver=1.9.23
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Template Model Builder: A General Random Effect Tool Inspired by 'ADMB'"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  blas
  lapack
  r
)
makedepends=(
  r-rcppeigen
)
optdepends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('c8db76a0cd1a1c043523ca81f5e6eca2')
b2sums=('0d7cebe9dde46e731712d8951932fa9abbfd8f0d8188fcd721aceca9ea6ce0bc25c45f2b5a6914b30948f0aa2426b85c354da0eeffa627bf091d807bb33d2d10')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

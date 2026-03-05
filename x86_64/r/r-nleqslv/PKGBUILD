# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nleqslv
_pkgver=3.3.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Solve Systems of Nonlinear Equations"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  lapack
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8f5cad9c43dc5360b37bf271607a9a19')
b2sums=('f1a3003ef330a03067c8f6830eb28a34d7c9a2e4ff5839dce0cec2264f07d444aa64e55af7adcc0989de0a7858fd91b6653ac791a22fec79a6026c5ff5e2b776')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

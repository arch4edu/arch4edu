# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=nleqslv
_pkgver=3.3.7
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
optdepends=(
  r-testthat
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('ec0e8fd1bafe686ed34d33298fbf02ed')
b2sums=('5d02914b55c13499412f9c1dc6a3e53ae7cdee2fc3b095a1c58b88a5ab369b04a06a86832f88ff1ae03d4e46e65949344f76981fa4f87c23544672a1e6d42124')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

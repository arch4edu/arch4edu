# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=deSolve
_pkgver=1.42
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Solvers for Initial Value Problems of Differential Equations ('ODE', 'DAE', 'DDE')"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  blas
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-fme
  r-scatterplot3d
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fd172c984a74de2fd7a456ad7e58c4d3')
b2sums=('565684542f4e3541912ef4388bda86eb07d8cbb6b4f73c7abc5d62053d49b3027b712708b095d98b2b2bb0d0a8e3e00144249ad266198d6db09cd8547c636c9e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

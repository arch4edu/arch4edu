# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ucminf
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="General-Purpose Unconstrained Non-Linear Optimization"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-numderiv
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('78b93a1975486d64c0534a1d8630e9da')
sha256sums=('5add8f84aeb0910a7ebf796c9514d4a3998606c3e45fe97e55d84f000a1d6df4')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

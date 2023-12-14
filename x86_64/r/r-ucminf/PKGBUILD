# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=ucminf
_pkgver=1.2.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
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
md5sums=('44871c91a7be26117ffad1e685a7b719')
sha256sums=('ed3ebba3d99a324444bd521d7aeb9f87344f44f170d67f77dab18dd3fbbfcc83')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

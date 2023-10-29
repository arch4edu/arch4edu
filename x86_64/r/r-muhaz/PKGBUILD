# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=muhaz
_pkgver=1.2.6.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hazard Function Estimation in Survival Analysis"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r
)
makedepends=(
  gcc-fortran
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6021d80354ee966f0d7be4ba6ce8c2d1')
sha256sums=('afa0102c13c108675c3f94a97bc17530bdf24fe3adef7623fbb06592bd42beb5')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

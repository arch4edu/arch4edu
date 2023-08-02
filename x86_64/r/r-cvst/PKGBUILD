# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=CVST
_pkgver=0.2-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Cross-Validation via Sequential Testing"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(GPL)
depends=(
  r-kernlab
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('08032c05dcea2d5ac36e119dcadca240')
sha256sums=('efa296230395f323c2a398a7b386e3a88e75a5b9b645307459d0b7c14d03f32d')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

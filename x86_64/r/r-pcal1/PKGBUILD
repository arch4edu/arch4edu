# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=pcaL1
_pkgver=1.5.10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="L1-Norm PCA Methods"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  blas
  coin-or-clp
  lapack
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0b5694d6d7ad7d615cf15b8f033f8086')
b2sums=('8ad8fae9fb1c0c7261e58fdd7ce94889752f902aeefa15b74563e09192a128ecb23bd3975efce2ee02fc5d0aa9a078c6feb10fc96b85eb562b2ecdea8a745ef2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

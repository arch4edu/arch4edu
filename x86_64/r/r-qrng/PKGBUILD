# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=qrng
_pkgver=0.0-10
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="(Randomized) Quasi-Random Number Generators"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only OR GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-copula
  r-randtoolbox
  r-spacefillr
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('513e4f9ab2775a64941dd45b943deea5')
b2sums=('282aeab39888dd61c9a42dd6a5429ad4f0364feb42b3a1b63134ab5844107e9fe9b1a1365e9d797603e4598dd1968162f8b2d0ecca34323ccb45f44dbf033e69')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

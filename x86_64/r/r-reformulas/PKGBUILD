# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=reformulas
_pkgver=0.4.3.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Machinery for Processing Random Effect Formulas"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r-rdpack
)
optdepends=(
  r-lme4
  r-testthat
  r-tinytest
  r-glmmtmb
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('877bcfda4d647182d2edf605f862361e')
b2sums=('18979947abfd5904786c231f19ed649364bdc5a2444557678d84c8707ea61435e62bb8096bc9db59730c7e3f86f532e681c1102efb794e380b87a07bba0b267a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

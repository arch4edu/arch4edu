# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=reformulas
_pkgver=0.4.2
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
  r-tinytest
  r-glmmtmb
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('60013679fc6245e945ead493b5c97b6a')
b2sums=('44202bdf86588fc2b7021b37a4927ba7523d8fda42a801f3ed4e37fd97af1e8af6f902b1385833f49524e996a98262c3fe6e40971749d31b91da8a0b2e844247')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

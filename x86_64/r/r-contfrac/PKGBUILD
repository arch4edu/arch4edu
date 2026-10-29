# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=contfrac
_pkgver=1.1-13
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Continued Fractions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f1471c7332f3308d5303178364bc645f')
b2sums=('2a01d21502394bbdd3cc8307660b09d6a248e6ee823628c462d88e7135b8563402a38caaf7ccc2d9def68dcf6e38a6a0f3479648ea88f8783089beeaac612399')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

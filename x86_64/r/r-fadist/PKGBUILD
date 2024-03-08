# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=FAdist
_pkgver=2.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=8
pkgdesc="Distributions that are Sometimes Used in Hydrology"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a7f13561055d26f9c11da8a494f3caca')
b2sums=('3a17d36346e87617b3c4b6e5c4cf0f092e18af0c87d36328c39487b194a05d657ca991c8e44cccc84434f7eb8760c11a0369a2d480a0df09d032546aeea640e5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

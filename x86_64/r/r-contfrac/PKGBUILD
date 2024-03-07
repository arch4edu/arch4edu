# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=contfrac
_pkgver=1.1-12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="Continued Fractions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8859a0eda910d18eb97683b535d2dc1d')
b2sums=('85b0c67ff26b6907b2634d1b6a1d38dbc0759b858c5152f2497a7ac43f50d603473025d19ff443a4d2be110a8f2fe8643b5dcb204f6c62873ff46198c10d908d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

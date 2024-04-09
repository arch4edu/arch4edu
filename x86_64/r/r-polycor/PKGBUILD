# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=polycor
_pkgver=0.8-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=6
pkgdesc="Polychoric and Polyserial Correlations"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-admisc
  r-mvtnorm
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bcf23e352787794c7e36875d6cd8d6f6')
b2sums=('040a667cc6a0dceeac6fe85e011e54605c081259f998deb8aae3be4f6c57820aa34f63f1b27c2e7a40e9099b35c8e57ba6b1d76488e6389a7f8eb0c2f80ed57a')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

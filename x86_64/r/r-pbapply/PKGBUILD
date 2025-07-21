# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pbapply
_pkgver=1.7-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Adding Progress Bar to '*apply' Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-future
  r-future.apply
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4cba88d695ff0beb228301caef295561')
b2sums=('b3f85eb9e8573b8e5b54cdfecfcab433c27c16dfcf9ef03f1009d65968ffadc08f8aef61690f32a65cd17c80f1729b5f723f9f0d29aa90815d45cd403d7a53a4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

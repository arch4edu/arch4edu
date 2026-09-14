# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=ca
_pkgver=0.72
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Simple, Multiple and Joint Correspondence Analysis"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-rgl
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('edb6a588903e1c0d1f703ee5de630ffc')
b2sums=('12877a905278d8f0d17e6beb2ddd8a422483ec41853049218a0216a58a6fe3fbe9239f722702f18bc1fe87608bb51434a544352209c8bb559c9b8258c5ce3e64')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: AutoUpdateBot <auto_update_bot@arch4edu.org>

_pkgname=orthopolynom
_pkgver=1.0-6.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Collection of functions for orthogonal and orthonormal polynomials"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
  r-polynom
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('043f7ec6fccafc90b2133c7f7f84c048')
b2sums=('20dfefac18f68a50d3e15887abe65e258b94604c9f2a20bb551a27bc393dca5962f8802df154ef31d90ed0d56bb713a71a40f1fcbd25f30f095331bcba2bbc12')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

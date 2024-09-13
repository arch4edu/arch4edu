# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Deriv
_pkgver=4.1.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Symbolic Differentiation"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('dcea8e11813976cd37a32a7b91781f52')
b2sums=('f34ae9b154d505d3d63dcb0516e341663ef3b029a5181c52b5421f1f14216e72853c94582aa0d67a46b46b4752b34a36713d1a53aa78c98942676e85145135b6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

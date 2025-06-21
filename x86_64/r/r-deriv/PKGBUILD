# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=Deriv
_pkgver=4.2.0
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
md5sums=('a6771b4d468d17d8faa0e516cd7427d9')
b2sums=('528e66537282845ffb5e37673e2f7d5112b00169b0001d2553644a8a469a64be6420ef45b4d2f2e18a7de4b26aef581b2ef7c7ebb56f9fd0b32a8b65ce417791')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

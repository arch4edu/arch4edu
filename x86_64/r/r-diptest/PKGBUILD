# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=diptest
_pkgver=0.77-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hartigan's Dip Test Statistic for Unimodality - Corrected"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6f36cb0d4e21c6766d5b8fcb73d8c1da')
b2sums=('1f65966aa3e7780ab3cc2636979bb63afab75f77b542b13a1dc168e0891cc0fe83f0cefeaf596ed867359909e0da2fbd7000e73d6967430e71169ed5f37a62bb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

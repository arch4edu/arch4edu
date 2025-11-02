# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Thomas Ivesdal-Tronstad <thotro at lyse dot net>

_pkgname=pracma
_pkgver=2.4.6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Practical Numerical Math Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-nlcoptim
  r-quadprog
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cd38dfab15df0e2fe0d56ac40644ef29')
b2sums=('3c22ee25e0a823c30b6f6a59b485559c69a02eaf3de86e19b65bdd6d2a520c7dd8c5aeeaf1f982d40b7efa455477bef963ba6f589784d381d8951b861785af07')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

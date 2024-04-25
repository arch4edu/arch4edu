# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Thomas Ivesdal-Tronstad <thotro at lyse dot net>

_pkgname=pracma
_pkgver=2.4.4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
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
md5sums=('f45e85a91a5e14b56a86191dd0bc9abd')
b2sums=('b68f72b31f410dd8b59f19dec8a5246a1b3e7c40abe0ded0fe2de9baa720230edfcedfea7fa10881434114bffa5733530ab54ddb98485f4c2db361ac8166a594')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

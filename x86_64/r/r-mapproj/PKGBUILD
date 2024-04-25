# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mapproj
_pkgver=1.2.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=4
pkgdesc="Map Projections"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(custom:LPL)
depends=(
  r-maps
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('df2ac0dd6e0cb2331f089c36041580f7')
b2sums=('bedcf9f5071a5052eb0184b63fdf55956c3e6601eb6fea3698a0af3f013914ae1def4f69a82d88880065f50a138029fdd968226897d3f2d86bdc844df94a6b23')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "$_pkgname/LICENSE.note"
}

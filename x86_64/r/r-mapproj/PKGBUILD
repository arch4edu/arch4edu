# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mapproj
_pkgver=1.2.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=3
pkgdesc="Map Projections"
arch=(x86_64)
url="https://cran.r-project.org/package=${_pkgname}"
license=(custom:LPL)
depends=(
  r-maps
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('df2ac0dd6e0cb2331f089c36041580f7')
sha256sums=('db2d201cc939de26717566066bf44225a967ccde6fc34731af845f03c086347d')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "$_pkgname/LICENSE.note"
}

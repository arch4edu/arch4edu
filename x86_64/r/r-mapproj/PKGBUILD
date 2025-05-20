# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=mapproj
_pkgver=1.2.12
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Map Projections"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=(custom:LPL)
depends=(
  r-maps
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('65f7a0098621af68e6fcd954d382a2f6')
b2sums=('d99c9432b88737beee35d44205cd02c8ad28254ab9aee0227deb32e950bcc4cb68db8a78d3d1845310b8dcb403f6a26577bc724ca930f693c8efa32658a69dd2')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "$_pkgname/LICENSE.note"
}

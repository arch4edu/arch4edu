# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=beeswarm
_pkgver=0.4.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=10
pkgdesc="The Bee Swarm Plot, an Alternative to Stripchart"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('Artistic-2.0')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('20c0aaccd552488e1f5ba7924d59ab33')
b2sums=('9ceeec0dc6dab75cad2c6b67da6656169cb8de231dcc3f9fab2ecb2241ac7dfe3d4647342928ac28b33c4db06538c5fef210d84924eb22249ef562ee90fac3a6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

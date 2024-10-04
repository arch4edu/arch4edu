# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Robert Greener <me@r0bert.dev>

_pkgname=rbibutils
_pkgver=2.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Read 'Bibtex' Files and Convert Between Bibliography Formats"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('2dfcf4f24b5409b826bd3ec8125fed4b')
b2sums=('fa9f1177ed696da5ef568da3a5d2ab390814458de47aa142eb451b6535c4fbf30a20e7abc158b4e8584600472d085fe1f007fe4ee9e7a5da40279c32b295fb2d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

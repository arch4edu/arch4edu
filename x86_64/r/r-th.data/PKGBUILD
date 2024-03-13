# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=TH.data
_pkgver=1.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=5
pkgdesc="TH's Data Archive"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-atr
  r-coin
  r-colorspace
  r-gridextra
  r-knitr
  r-multcomp
  r-rms
  r-tram
  r-trtf
  r-vcd
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('4e6e59fee15e056be3721f7c0d4e017c')
b2sums=('c091698b1761d54e8281b6fc74466ec5f000ccb71e143e9aeef50125154012d391cf93e4b71661301f896ce46d8fcd94459dff8a1596565c1ab705f9a98ddb7b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

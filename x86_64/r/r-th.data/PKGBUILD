# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=TH.data
_pkgver=1.1-3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
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
md5sums=('5b984967b15c3e2da7b3fa7534e64673')
b2sums=('aca87b54b9e0e5f5aa20d62a29a9c32043195a00b4177d4e3b991cc01bafd9d0ac4c6ae37544499a7eaec286c98d008552271e696e6af15e34f49fa18d5bd005')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

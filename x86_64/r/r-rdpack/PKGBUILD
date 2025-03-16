# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=Rdpack
_pkgver=2.6.3
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Update and Manipulate Rd Documentation Objects"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rbibutils
)
optdepends=(
  r-gbrd
  r-rprojroot
  r-rstudioapi
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b43e5be13fb94da72ad9549eab5218ff')
b2sums=('2f5ebe50624fd1a5dd262dc327a7e4cecce721279ffe28715e96a1b01d8f721f454c5b5e8c87ec2c7303cd4ed0b4abe2845b30b051432bf7681aadea9ecd3a89')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

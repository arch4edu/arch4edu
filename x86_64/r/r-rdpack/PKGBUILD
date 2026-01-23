# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=Rdpack
_pkgver=2.6.5
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
md5sums=('866e1adfb8171aac20c34e250976ae63')
b2sums=('1c499193788f8fd3946e496827fed4e0eeb437ca30856b9cb86b1b995d68b385f25e9610ca256f1c15a1a6fcc867249fca6387d8588c27a940da9bfec1f4e080')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

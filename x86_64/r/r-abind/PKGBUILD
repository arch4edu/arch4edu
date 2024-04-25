# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Taekyung Kim <Taekyung.Kim.Maths@gmail.com>
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=abind
_pkgver=1.4-5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Combine Multidimensional Arrays"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('136f981e1c4f618b64a87faaa7797c97')
b2sums=('64228df7f46f0fce03d8c33c8655bb7d239a5d25db5c93cfe56942a2db8917698a5b4fb6e6a8a40c0f6bec9ed2d8a5923473a5813d6a9d8f5901a2f8fdcb260f')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

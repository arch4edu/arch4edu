# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Phil Schaf <flying-sheep@web.de>

_pkgname=fdrtool
_pkgver=1.2.18
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Estimation of (Local) False Discovery Rates and Higher Criticism"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('abf828d9e46b2c7a512950635a1441a9')
b2sums=('50ac969c0a1e8026132cb533e629360573311cbd510652fd583edbf60ba084823a61a31ac8871c8c76d70626d2305820a20e81701e7ed5bc0606fe9c770923a6')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

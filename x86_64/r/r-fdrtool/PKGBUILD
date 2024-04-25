# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Phil Schaf <flying-sheep@web.de>

_pkgname=fdrtool
_pkgver=1.2.17
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Estimation of (Local) False Discovery Rates and Higher Criticism"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7e4ee6e67266b8828cc9d893a171545e')
b2sums=('0ea74bed7a0feb8b712aafcdbdf9ca1a6fc9590896fd61a8531c8dfc18c921db34fa99abcb1047edf9c665d18d92ac7e1f47bc5a216926f51e5788dc7a3b7e53')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=parallelly
_pkgver=1.45.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Enhancing the 'parallel' Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
optdepends=(
  r-base64enc
  r-commonmark
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('cbcc6d61a320c8871c01f7ad6d942bc8')
b2sums=('7964e21fc6a32ae38570cd5f13ca2175fcea229a65fcaa57f2b07c04b89510496e0766d6a5c356dad3ddf8f7746d9814a01aa47e4e734d4a21a990e4040a837e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=maxstat
_pkgver=0.7-26
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Maximally Selected Rank Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-exactranktests
  r-mvtnorm
)
optdepends=(
  r-th.data
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b8c781c2eb9317bd03387012b79f5ca7')
b2sums=('0869820cd646b18ea6e19d201998f142e7a8329172cf9a5b1b3a50c703bfdbe4c565fb0d3d598a3c9477629680f3e996eaa08dc90d0910292270bc45799b8d26')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=stabledist
_pkgver=0.7-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Stable Distribution Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-fbasics
  r-fmstable
  r-libstable4u
  r-rmpfr
  r-runit
  r-sfsmisc
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('15153e639dd4358143f069cceacef6d3')
b2sums=('439c087a8d454d9bebb8a0a83ef60fba098ca828312f890fe921a5485a29c956fda6a51a1bbbd11319951ddb03e2eee070c0952925418578e58451af95f3e9c4')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

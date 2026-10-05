# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=listenv
_pkgver=1.1.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Environments Behaving (Almost) as Lists"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('Apache')
depends=(
  r
)
optdepends=(
  r-markdown
  r-r.rsp
  r-r.utils
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d46f5ee5a4fe464bb52a2a17289b7818')
b2sums=('1fac1fad7c3d97d1c9f09ac3e04e1961fb4d079e445fe2ee196d691f441fbe7b6282a75b958e6b17012aae0f2dc41915ea8cf26b13fac7836bc2a1b43298934e')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

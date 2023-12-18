# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=listenv
_pkgver=0.9.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Environments Behaving (Almost) as Lists"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=(LGPL)
depends=(
  r
)
optdepends=(
  r-markdown
  r-r.rsp
  r-r.utils
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('e0ab27f35467ce48ad347758f4e1e8d8')
b2sums=('d2692bb7fe41f738a6751ec8a067764405451bef1b4e558f77564c657e773ed30ef3453f6e39a39ead919885bccdaeb9356229fcb5e8c490864245d4e38f8426')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

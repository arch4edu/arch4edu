# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=libcoin
_pkgver=1.0-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Linear Test Statistics for Permutation Inference"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-mvtnorm
)
optdepends=(
  r-bibtex
  r-coin
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('8f6a6c0819329aff66ea35f91cda5aca')
b2sums=('763e764b8556c63de6a84a1609b1f490ca65c5b9cd5bc10558cc7f11ac75820227d3bae6af7844376f52586794b5b7bb9441fc842f7496f13d3cd957e905e117')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=graph
_pkgver=1.84.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="A package to handle graph data structures"
arch=(x86_64)
url="https://bioconductor.org/packages/$_pkgname"
license=('Artistic-2.0')
depends=(
  r-biocgenerics
)
optdepends=(
  r-biocstyle
  r-knitr
  r-rbgl
  r-runit
  r-sparsem
  r-xml
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7bc1f44620e332c21594a946d8990062')
b2sums=('7d20a88ef5da27f622ca52345144c5605cf1efd3d356bbf9a7652a86336eba6bbc1ccfa776490214cffa5317497e5ff2bc096462a47cb0653dd614b7fe69373c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

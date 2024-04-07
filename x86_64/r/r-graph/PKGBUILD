# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=graph
_pkgver=1.80.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
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
md5sums=('735b96df0f7c955806148170220b75b2')
b2sums=('67c60fe3b3160bbe16db9e5e31e7d85d8fa4bd812a39dce1ac7c57bb8dbe5789abd2e983b595e0d68a87087effc34550060ddd9d6e95dcb4a3f46154a3c7a77b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

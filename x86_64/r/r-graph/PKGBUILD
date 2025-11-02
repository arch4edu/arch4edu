# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=graph
_pkgver=1.88.0
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
md5sums=('c6dcb5fc44a32acad2acf8fb09ff675a')
b2sums=('b9eb44804ea155c2939199d73e725714b9f309acc1296a37fc94aa43888bcc5f666b9a479aa5b3d2a6b56c0953d2868f280d1b1fa9b2cb441f773d41ef70954c')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

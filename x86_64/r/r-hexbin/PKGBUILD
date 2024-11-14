# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=hexbin
_pkgver=1.28.5
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Hexagonal Binning Routines"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-affy
  r-biobase
  r-knitr
  r-limma
  r-marray
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('fb006a74ba94bccdc610baf1e182a918')
b2sums=('81b75141896217fccb3b70b69dddfab03497affd6ab264651f902cf74e65a51ede0c2aacd99d041b0243fa140208754f03a14618fd07c53165de77f845021407')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

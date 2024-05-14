# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vegan
_pkgver=2.6-6
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Community Ecology Package"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  lapack
  r-permute
)
makedepends=(
  gcc-fortran
)
optdepends=(
  r-knitr
  r-markdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('b2d094ff5dbba88479f323459f5d5b63')
b2sums=('d2310988ca8aa3101e4fef936b7242d884ce045342c8fe3106f8eb59cbf2446d7cef24801b5060ec4973d3d035ed7043facfe73dd094d62b98e787776c5a3e16')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

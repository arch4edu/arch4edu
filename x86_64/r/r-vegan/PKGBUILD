# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=vegan
_pkgver=2.6-6.1
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
md5sums=('acd593d013bb8f8e5ac057ec70d9cd4b')
b2sums=('09be57a31c25619f37bc2a9b991962637dd0d206db0f2ca703226f3cc0f3c884a6c1589c31e6a646d34dd92cde4f4d7d4b8ebd56f208a1ba21a9db2f5c7de024')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

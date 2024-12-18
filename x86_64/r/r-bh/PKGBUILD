# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_pkgname=BH
_pkgver=1.87.0-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Boost C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSL-1.0')
depends=(
  boost
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('55959f3c42d4229724aa73b450c881fe')
b2sums=('5acb19b106933f72e8f90a4f006b477cbf47fb16f4ce1441817b66fba7839f3444134698ea635dd98501fc3596575d6c00cbbb1d9e01bafaf6b44151bd85757d')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  # Use system boost headers from the `boost` package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/include"
  rm -r boost
  ln -s /usr/include/boost
}

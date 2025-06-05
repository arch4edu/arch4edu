# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=stringmagic
_pkgver=1.2.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Character String Operations and Interpolation, Magic Edition"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rcpp
)
optdepends=(
  r-data.table
  r-knitr
  r-rmarkdown
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('0f58ab4c2367d17ecb078080536cc7ce')
b2sums=('daeceb94ef395ede0855ce2b0fd2e0cfb15bdc178d6982228e39878e6583ce4daeaee9a4615bb13674e3eed0cf978f5422ad79ef78d5c999ffc0c4ab4861ab21')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

check() {
  cd "$_pkgname/tests"
  R_LIBS="$srcdir/build" Rscript --vanilla stringmagic_tests.R
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=bigassertr
_pkgver=0.1.7
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Assertion and Message Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-covr
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('6361d2f8f589ea5657a73c9d81668e11')
b2sums=('d525055d9bbcdfc5a7d4f3c8db23bfb8432f5de7c18285f07ae182d7f2beb36542368081785fd9c28381d4c2244611d24a57e8176d147195646a996c3c18d0dd')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Alex Branham <branham@utexas.edu>

_pkgname=inline
_pkgver=0.3.21
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Functions to Inline C, C++, Fortran Function Calls from R"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-rcpp
  r-tinytest
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('acc2b04335978bf903c952d2a5139cd5')
b2sums=('98df8e21aa30be8af0d0b52d9b50595b0d1610aff7c4bf8f359a8abc59a55d11cca3a55ba3410bb91c3ab22722890798f4ee0e081bdcbf535fce1851ce59b9ae')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

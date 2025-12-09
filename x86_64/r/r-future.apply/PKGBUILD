# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_pkgname=future.apply
_pkgver=1.20.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Apply Function to Elements in Parallel using Futures"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-future
  r-globals
)
optdepends=(
  r-listenv
  r-markdown
  r-r.rsp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('f11d246097d85dae24017971bb23bf7e')
b2sums=('6aceef90df3a37ee9a80ec584b7a48fdb71e533d7a3efdfb4326429112e0ebf55709ff677e9332fac7dacaa2fd3dabacfe59f675946ea2b0335c28d6516f25a5')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

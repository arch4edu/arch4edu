# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Robert Greener <me@r0bert.dev>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=Rdpack
_pkgver=2.6.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Update and Manipulate Rd Documentation Objects"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-rbibutils
)
optdepends=(
  r-gbrd
  r-rprojroot
  r-rstudioapi
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('bf0795c0b798cffbac6dc284a7752d54')
b2sums=('30b80bf265c1d999c55209868c1e06a8308d0bf1efd2a3ccb1d0d322d7443ec99938afb5e70433f19b34ad5f19d8f85cefc239f3301f561522f1c2628775c178')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

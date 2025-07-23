# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=AcceptanceSampling
_pkgver=1.0.11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Creation and Evaluation of Acceptance Sampling Plans"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('880e18eb33ee15fef2d77bedf4cc6087')
b2sums=('a9236ce6568c4a088e7ac90ad6e17a7a1f786407402dd163ca12503100a0de659aea25db5e93b013970fd5a7687f4b29e529d63a090f882f965a5ecb1611ccc1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

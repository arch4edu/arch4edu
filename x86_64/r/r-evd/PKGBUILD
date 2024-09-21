# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=evd
_pkgver=2.3-7.1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Functions for Extreme Value Distributions"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-only')
depends=(
  r
)
optdepends=(
  r-interp
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('95f8e58d5126ccb82f8e458430a3ead2')
b2sums=('d0667c09455d4c728355637d87223c7970744b8c87b9d83889d08be7a455af43829736ce03275ec81e279b01ecffa26e7e8f237f8e6657f37377e7a6714dc28b')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

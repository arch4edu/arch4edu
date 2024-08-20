# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjson
_pkgver=0.2.22
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="JSON for R"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('05f4789a20d1d9fcbb587a129172e08d')
b2sums=('b9b79adae1c024e1537e04da4a302ffb4ff3a48423dab60b09dca0a9c82ef30f55e78c98963bd461c3e5eeca40e3601653de5712ce8b9f96d231e43db6f2a5e1')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

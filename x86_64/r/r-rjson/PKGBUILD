# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=rjson
_pkgver=0.2.23
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
md5sums=('3eccfd8c0623a5c7ea7456b585d43dbe')
b2sums=('e7a0da1dbc003419d682755fb4374db8a52c310df79e7af13896121e328a006e2ba612420b27b91d7cad3a092eaf49d83a6ad5b76879ad173e4b56cf40122aee')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

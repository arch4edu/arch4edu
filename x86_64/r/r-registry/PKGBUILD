# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=registry
_pkgver=0.5-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=11
pkgdesc="Infrastructure for R Package Registries"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-only')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7ae0c72093167cee00545d49511c4c0b')
b2sums=('b88ab31e625802664f018b30cc9cd2cbef22fa1ba44355716c74f06024bc7b7e16bf0afaf7543b61d4ac38f63837d54c4ee5900cd1ac92a1ffccdce6b9d28a95')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

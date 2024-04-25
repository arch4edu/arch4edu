# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=pbapply
_pkgver=1.7-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="Adding Progress Bar to '*apply' Functions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-future
  r-future.apply
  r-shiny
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('76c7702f9ffb732731c431ee4b6fdfb2')
b2sums=('c7f9ea987824de96a46d6fed40d12102c6f378cc5e4db41fddb7ceccdb36f2aa0891b7ebd940252c75340d43c7ad183c63e7f04f6e53618c2e94db0fbb5decfc')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Guoyi Zhang <guoyizhang at malacology dot net>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_pkgname=globals
_pkgver=0.20.0
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Identify Global Objects in R Expressions"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('LGPL-2.1-or-later')
depends=(
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7f5bcbc401ed1bf3d12f730446bc8fa9')
b2sums=('37985bf53ad1267732af8006535e8b875b720004bc43a37c89d24f64c9468a7f58a5050a6c1bf0f9e104aa585ec30434cd831a6ed1e3c57eb84edca1373372f8')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

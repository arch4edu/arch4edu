# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=RANN
_pkgver=2.6.2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Fast Nearest Neighbour Search (Wraps ANN Library) Using L2 Metric"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-3.0-or-later')
depends=(
  r
)
optdepends=(
  r-testthat
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('d5a42d1f730a34f7298318996eae7c63')
b2sums=('c71a5b041c6ee378e7452b3e63c308d768b6280f93a001387daad8bf14db2a78832b3114eabcc98d3278fccde2334c7f21403b2de2f2cf7986c305194f51e830')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

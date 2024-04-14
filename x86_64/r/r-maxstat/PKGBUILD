# Maintainer: Guoyi Zhang <guoyizhang at malacology dot net>

_pkgname=maxstat
_pkgver=0.7-25
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=7
pkgdesc="Maximally Selected Rank Statistics"
arch=(x86_64)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r-exactranktests
  r-mvtnorm
)
optdepends=(
  r-th.data
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('35b234371e4321d98e7659d2f3a35546')
b2sums=('b5e5e9dfd2ad959b3fc0acba1379ae27f004f6d7b2babcadec35cb730fcc278ba1ad032800c6f62e324ed1a478b8597334a96a730e905a513b5cb2c45227e4cb')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

# Maintainer: sukanka <su975853527@gmail.com>

_pkgname=mdscore
_pkgver=0.1-4
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="Improved Score Tests for Generalized Linear Models"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('GPL-2.0-or-later')
depends=(
  r
)
optdepends=(
  r-sleuth3
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('a86703826f3030a00810df2c7baa8f49')
b2sums=('b3f1ee7fb3c0797ec44b124d75f4cc28dfc5b8b20310bb4ad9e286473469bc22bef2a3ccfa08ede3a8776399cf93adbd1176264041219dc4a0782fc19c6426ed')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"
}

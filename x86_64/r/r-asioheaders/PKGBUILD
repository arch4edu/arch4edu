# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AsioHeaders
_pkgver=1.30.2-1
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=1
pkgdesc="'Asio' C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSL-1.0')
depends=(
  asio
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('5c4346bc1746a3b55e0fdf1608460b55')
b2sums=('dd4ea05bcf769a0907a4296798466408db252dd94c0903d7f77af083356ac3ca8dde82c16530be7675ee34e22494e9c3f59af785d66c2616badfe03fff72b039')

build() {
  mkdir build
  R CMD INSTALL -l build "$_pkgname"
}

package() {
  install -d "$pkgdir/usr/lib/R/library"
  cp -a --no-preserve=ownership "build/$_pkgname" "$pkgdir/usr/lib/R/library"

  # devendor header files by linking to 'asio' package
  cd "$pkgdir/usr/lib/R/library/$_pkgname/include"
  rm -r asio asio.hpp
  ln -s /usr/include/asio
  ln -s /usr/include/asio.hpp
}

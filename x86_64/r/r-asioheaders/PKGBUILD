# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AsioHeaders
_pkgver=1.22.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc="'Asio' C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=$_pkgname"
license=('BSL-1.0')
depends=(
  asio
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7e7f8f45115ba4e62334b225ee859cb0')
b2sums=('50f22f2b5ac13b9240f3ef9bdf02717962bc53eaa447a4411d8cf88e1eb17bd3f75291d3bfb0de77f28aa9cc3c8f8416068ef82c3b20edb81aa9ffc13991c81a')

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

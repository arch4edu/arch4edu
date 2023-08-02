# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AsioHeaders
_pkgver=1.22.1-2
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//-/.}
pkgrel=2
pkgdesc="'Asio' C++ Header Files"
arch=(any)
url="https://cran.r-project.org/package=${_pkgname}"
license=(Boost)
depends=(
  asio
  r
)
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
md5sums=('7e7f8f45115ba4e62334b225ee859cb0')
sha256sums=('1629c0ea78b8c63231ca62fcc39fce5d29919864050a8c331720ee9bbdea58a4')

build() {
  mkdir -p build
  R CMD INSTALL "$_pkgname" -l build
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

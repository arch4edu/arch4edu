# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>

_pkgname=AsioHeaders
_pkgver=1.28.2-1
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
md5sums=('beed8f564d27682a13b672b19e2f002c')
b2sums=('57846e6296d8ed0070befe6d97d01a670aac26350e3aab58476cb1887b49102e27cef03705672bdd9fc25b496c967bf62236dced365ef92c5547ec1d4f1c3c68')

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

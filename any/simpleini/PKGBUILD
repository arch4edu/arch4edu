# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.19
pkgrel=1
pkgdesc="Cross-platform C++ library providing a simple API to read and write INI-style configuration files"
arch=('any')
url="https://github.com/brofield/simpleini"
license=('MIT')
depends=()
makedepends=()
optdepends=()
source=(https://github.com/brofield/simpleini/archive/$pkgver.tar.gz)
sha256sums=('dc10df3fa363be2c57627d52cbb1b5ddd0689d474bf13908e822c1522df8377e')

package() {
  install -D -m644 "${srcdir}"/"${pkgname}"-"${pkgver}"/SimpleIni.h "${pkgdir}"/usr/include/SimpleIni.h
  install -D -m644 "${srcdir}"/"${pkgname}"-"${pkgver}"/ConvertUTF.h "${pkgdir}"/usr/include/ConvertUTF.h
  install -D -m644 "${srcdir}"/"${pkgname}"-"${pkgver}"/ConvertUTF.c "${pkgdir}"/usr/src/SimpleIni/ConvertUTF.c
  install -D -m644 "${srcdir}"/"${pkgname}"-"${pkgver}"/LICENCE.txt "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENCE.txt
}

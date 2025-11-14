# Contributor: robertfoster
# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.25 # renovate: datasource=github-tags depName=brofield/simpleini
pkgrel=2
pkgdesc="Cross-platform C++ library providing a simple API to read and write INI-style configuration files"
arch=('x86_64' 'aarch64')
url="https://github.com/brofield/simpleini"
license=('MIT')
makedepends=('cmake' 'gtest')
source=("${url}/archive/refs/tags/v$pkgver.tar.gz")

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cmake . -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DINSTALL_GTEST=OFF \
    -DSIMPLEINI_USE_SYSTEM_GTEST=ON
  cmake --build build
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  DESTDIR="${pkgdir}" \
    cmake --install build

  install -D -m644 ConvertUTF.c \
    "${pkgdir}"/usr/include/SimpleIni"/ConvertUTF.c"
  install -D -m644 ConvertUTF.h \
    "${pkgdir}"/usr/include/SimpleIni"/ConvertUTF.h"

  install -D -m644 LICENCE.txt \
    "${pkgdir}"/usr/share/licenses/${pkgname}"/LICENSE.txt"
}

sha256sums=('10001ee1486ae55259a5408786262bc0f72d699bc9637d536ebc62765d3ecd3b')

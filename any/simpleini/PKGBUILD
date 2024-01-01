# Contributor: robertfoster
# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.22
pkgrel=1
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

  install -D -m644 LICENCE.txt \
    "${pkgdir}"/usr/share/licenses/${pkgname}"/LICENSE.txt"
}

sha256sums=('b3a4b8f9e03aabd491aa55fd57457115857b9b9c7ecf4abf7ff035ca9d026eb8')

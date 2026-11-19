# Contributor: robertfoster
# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.28 # renovate: datasource=github-tags depName=brofield/simpleini
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

sha256sums=('ec14f7b2c706d798a051b0b75561b1cec8e616cee1021f900767244f59f96a79')

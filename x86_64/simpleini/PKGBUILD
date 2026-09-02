# Contributor: robertfoster
# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.27 # renovate: datasource=github-tags depName=brofield/simpleini
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

sha256sums=('bcf27c6ccab787cb41ee2af430d271b4b483319529978e4e2b1770f14db5627b')

# Contributor: robertfoster
# Maintainer: Tobias Borgert <tobias.borgert@gmail.com>

pkgname=simpleini
pkgver=4.26 # renovate: datasource=github-tags depName=brofield/simpleini
pkgrel=3
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

sha256sums=('cfb27ba82570d73ce89d956f15c558d4a79c7ce2ad667a104be2d2f0f12be0cb')

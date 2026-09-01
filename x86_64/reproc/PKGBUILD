# Maintainer: Javier Tia <javier dot tia at gmail dot com>
# Contributor: Daan De Meyer <daan.j.demeyer@gmail.com>

pkgname=reproc
pkgver=14.2.8
pkgrel=1
pkgdesc='Cross-platform library that simplifies working with external CLI applications from C and C++'
arch=('x86_64')
url='https://github.com/DaanDeMeyer/reproc'
license=('MIT')
depends=('gcc-libs' 'glibc')
makedepends=('cmake')
# Upstream tagged 14.2.8 without the historical "v" prefix; the source path
# tracks the bare tag name (nvchecker strips the prefix, so ${pkgver} matches).
source=("${url}/archive/${pkgver}.tar.gz")
sha256sums=('27c3b452bfc419a2deda23969aa10c77909c4ff9e71c549eb65d09ae6aa7aa32')

build() {
  cmake \
    -S "${pkgname}-${pkgver}" \
    -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_SHARED_LIBS=ON \
    -DREPROC++=ON \
    -DREPROC_TEST=ON \
    ../
  cmake --build build
}

check() {
  cmake --build build --target test
}

package() {
  DESTDIR="${pkgdir}" cmake --install build
  install -D --mode=644 "${srcdir}/${pkgname}-${pkgver}"/LICENSE \
    "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE
}

# vim:set ts=2 sw=2 et:

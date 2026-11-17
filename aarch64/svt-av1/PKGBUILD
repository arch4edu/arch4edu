# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Daniel Bermond <dbermond@archlinux.org>
# Contributor: Thomas Schneider <maxmusterm@gmail.com>

pkgname=svt-av1
pkgver=4.3.0
pkgrel=1
pkgdesc='Scalable Video Technology AV1 encoder and decoder'
arch=(x86_64)
url=https://gitlab.com/AOMediaCodec/SVT-AV1
license=(
  BSD-3-Clause
  LicenseRef-AOMPL-1.0
)
depends=(glibc)
makedepends=(
  cmake
  git
  nasm
  ninja
)
source=(git+https://gitlab.com/AOMediaCodec/SVT-AV1.git#tag=v${pkgver})
b2sums=('42c2367abb2134833c332cc93b6d3f6a202fb085adeaa1dedf2afa47fbf353a8fde42e1c884f5ec6fd37b12a26c97b435ac12cf59d65188f842ca380ac60f2bf')

prepare() {
  sed '/CMAKE_BUILD_TYPE Release/d' -i SVT-AV1/CMakeLists.txt
}

build() {
  cmake -S SVT-AV1 -B build -G Ninja \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DNATIVE=OFF
  ninja -C build
}

package() {
  DESTDIR="${pkgdir}" ninja -C build install
  install -Dm 644 SVT-AV1/{LICENSE,PATENTS}.md -t "${pkgdir}"/usr/share/licenses/svt-av1/
}

# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Daniel Bermond <dbermond@archlinux.org>
# Contributor: Thomas Schneider <maxmusterm@gmail.com>

pkgname=svt-av1
pkgver=4.2.0
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
b2sums=('b217f854d8e97323bdc4327309a485c6821421e43d077be41ced99b0e4d2e4c46d4593a919afb0db8e89e35e23544bac22fe751e78996a62ef3d1ef8895509de')

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

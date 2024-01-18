# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alfredo Luque <me@aluque.io>>

pkgname=cctz
pkgver=2.3
pkgrel=5
pkgdesc="A C++ library for translating between absolute and civil times using the rules of a time zone"
arch=(x86_64)
url="https://github.com/google/cctz"
license=('Apache-2.0')
depends=(
  gcc-libs
)
makedepends=(
  benchmark
  cmake
  gtest
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('e688ddac1bff108e8315bf94cb61483b72b0d16f601e4e1eeb0fd5c064aefe5a573eee66e8903401aa4c2be71ea9f10dd6c9a9cdf8379f5bb6073248a21a83ff')

prepare() {
  cd "$pkgname-$pkgver"
  # Set shared library version and soversion
  sed -i '/set_target_properties(cctz/a\ \ VERSION ${VERSION}\n  SOVERSION ${SOVERSION}' \
      CMakeLists.txt

  # Use system zoneinfo data in tests
  sed -i 's|TZDIR=${CMAKE_CURRENT_SOURCE_DIR}/testdata/zoneinfo|TZDIR=/usr/share/zoneinfo|' \
      CMakeLists.txt
}

build() {
  cmake -B build -S "$pkgname-$pkgver" \
      -DCMAKE_BUILD_TYPE='None' \
      -DCMAKE_CXX_FLAGS_INIT=-DNDEBUG \
      -DCMAKE_INSTALL_PREFIX='/usr' \
      -DBUILD_SHARED_LIBS=ON \
      -DBUILD_EXAMPLES=OFF \
      -DVERSION="$pkgver" \
      -DSOVERSION="${pkgver%%.*}" \
      -Wno-dev
  cmake --build build
}

check() {
  cd build
  ctest --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}

# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Alfredo Luque <me@aluque.io>>

pkgname=cctz
pkgver=2.4
pkgrel=2
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
sha512sums=('6d50fe5263b66f93bc3f9aee0da395352d0e95187e6a761afd1b82a461c127823fe93e06139e9d8989f24875b70de3058aab6e66639b408c7930f117e1815e5e')

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
  #ctest --output-on-failure
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}

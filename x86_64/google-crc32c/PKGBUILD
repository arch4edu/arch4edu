# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Morteza NourelahiAlamdari <m@0t1.me>

pkgname=google-crc32c
pkgver=1.1.2
pkgrel=4
pkgdesc="CRC32C implementation with support for CPU-specific acceleration instructions"
arch=(x86_64)
url="https://github.com/google/crc32c"
license=(BSD)
depends=(
  gcc-libs
)
makedepends=(
  cmake
)
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('ac07840513072b7fcebda6e821068aa04889018f24e10e46181068fb214d7e56')

prepare() {
  # fix version
  sed -i "s/Crc32c VERSION 1.1.0 /Crc32c VERSION $pkgver /" "crc32c-$pkgver/CMakeLists.txt"
}

build() {
  cmake -B build -S "crc32c-$pkgver" \
      -DCMAKE_BUILD_TYPE=None \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DBUILD_SHARED_LIBS=yes \
      -DCRC32C_BUILD_TESTS=OFF \
      -DCRC32C_BUILD_BENCHMARKS=OFF \
      -DCRC32C_USE_GLOG=OFF \
      -DCRC32C_INSTALL=ON \
      -Wno-dev
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" "crc32c-$pkgver/LICENSE"
}

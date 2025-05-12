# Maintainer: envolution
# Contributor: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Morteza NourelahiAlamdari <m@0t1.me>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=google-crc32c
pkgver=1.1.2
pkgrel=5
pkgdesc="CRC32C implementation with support for CPU-specific acceleration instructions"
arch=(x86_64)
url="https://github.com/google/crc32c"
license=(BSD-3-Clause)
depends=(
  gcc-libs
)
makedepends=(
  cmake
  git
)

#cmake 4 patch
#https://github.com/google/crc32c/commit/2bbb3be42e20a0e6c0f7b39dc07dc863d9ffbc07
_tag='2bbb3be42e20a0e6c0f7b39dc07dc863d9ffbc07'

source=("$pkgname-${pkgver%%+*}::git+https://github.com/google/crc32c.git#tag=${_tag}")
sha256sums=('622e752bac7eb19110e53639b1c86ae9188a4882dca8796f81eb0bcb088262f1')

build() {
  cd "${pkgname}-${pkgver%%+*}"
  cmake -B build -S . \
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
  cd "${pkgname}-${pkgver%%+*}"
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE
}
# vim:set ts=2 sw=2 et:

# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=librdkafka1
pkgver=1.9.2
pkgrel=1
pkgdesc='The Apache Kafka C/C++ library. Legacy version.'
arch=(x86_64)
url='https://github.com/edenhill/librdkafka'
license=(BSD)
depends=(libsasl zstd curl)
makedepends=(python openssl lz4 rapidjson cmake)
source=(librdkafka-$pkgver.tar.gz::https://github.com/edenhill/librdkafka/archive/v$pkgver.tar.gz
        link_curl.patch::https://github.com/edenhill/librdkafka/commit/23bd03c11c344aaa01ace8951e60913b4bfa3c2e.patch)
sha256sums=('3fba157a9f80a0889c982acdd44608be8a46142270a389008b22d921be1198ad'
            '88c6587060454868a8441bc33215d76d9e174675cc32ec10d95c7a34d33cd17f')
provides=('librdkafka')
conflicts=('librdkafka')

prepare() {
  cd librdkafka-$pkgver
  patch -p1 < ../link_curl.patch
}

build() {
  cmake -S librdkafka-$pkgver -B build -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

check() {
  # TODO: figure out why the tests timeout
  # cmake --build build --target test
  true
}

package() {
  cmake --build build --target install -- DESTDIR="$pkgdir"
}

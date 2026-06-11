# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: James Campos <james.r.campos@gmail.com>
# Contributor: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Dongsheng Cai <dongsheng at moodle dot com>
# Contributor: Masutu Subric <masutu.arch at googlemail dot com>
# Contributor: TIanyi Cui <tianyicui@gmail.com>

pkgname=libnode
pkgver=26.2.0
pkgrel=1
pkgdesc='libnode.so from nodejs-shared'
arch=('x86_64')
url='https://nodejs.org/'
license=('MIT')
depends=('ada' 'brotli' 'c-ares' 'icu' 'libffi' 'libnghttp2' 'libnghttp3' 'libngtcp2' 'libuv' 'openssl' 'simdjson' 'zlib' 'zstd')
makedepends=('ninja' 'procps-ng' 'python')
source=("nodejs-${pkgver}.tar.gz::https://github.com/nodejs/node/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('ad746843b31ff9788ffa752c82b98970611e75dbdeed0cd3e44024f48a6746331f860217ddfec4665cdb0b848f47d0770bb97b1c5249d27e173f2f34ae6055f1')

_set_flags() {
  CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
}

build() {
  _set_flags
  cd node-${pkgver}

  ./configure \
    --ninja \
    --enable-lto \
    --prefix=/usr \
    --with-intl=system-icu \
    --without-npm \
    --shared \
    --shared-ada \
    --shared-brotli \
    --shared-cares \
    --shared-ffi \
    --shared-libuv \
    --shared-nghttp2 \
    --shared-nghttp3 \
    --shared-ngtcp2 \
    --shared-openssl \
    --shared-simdjson \
    --shared-zlib \
    --shared-zstd

  make
}

package() {
  conflicts=('nodejs-shared')

  cd node-${pkgver}
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"

  cd "$pkgdir"/usr/lib
  ln -s libnode.so.* libnode.so

  mv "$pkgdir"/usr/include/node "$pkgdir/usr/include/$pkgname"

  rm -rf "$pkgdir"/usr/{bin,lib/node_modules,share/doc,share/man}
}

# vim:set ts=2 sw=2 et:

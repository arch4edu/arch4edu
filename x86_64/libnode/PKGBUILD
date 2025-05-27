# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: James Campos <james.r.campos@gmail.com>
# Contributor: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Dongsheng Cai <dongsheng at moodle dot com>
# Contributor: Masutu Subric <masutu.arch at googlemail dot com>
# Contributor: TIanyi Cui <tianyicui@gmail.com>

pkgname=libnode
pkgver=23.11.1
pkgrel=1
pkgdesc='libnode.so from nodejs-shared'
arch=('x86_64')
url='https://nodejs.org/'
license=('MIT')
options=(!lto)
depends=('icu' 'libuv' 'libnghttp2' 'libnghttp3' 'libngtcp2' 'openssl' 'zlib' 'brotli' 'c-ares') # 'http-parser' 'v8')
makedepends=('python' 'procps-ng')
source=("nodejs-${pkgver}.tar.gz::https://github.com/nodejs/node/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('9003d38c888d23224c5d238bc59fcb5f3afa586bee3de00196a196e7db14c243b16cee47a09d669e32aa07144250af48e5aa4d00762015fe1049fba907eb685f')

build() {
  cd node-${pkgver}

  # /usr/lib/libnode.so uses malloc_usable_size, which is incompatible with fortification level 3
  export CFLAGS="${CFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"
  export CXXFLAGS="${CXXFLAGS/_FORTIFY_SOURCE=3/_FORTIFY_SOURCE=2}"

  ./configure \
    --prefix=/usr \
    --without-npm \
    --with-intl=system-icu \
    --shared \
    --shared-libuv \
    --shared-nghttp2 \
    --shared-nghttp3 \
    --shared-ngtcp2 \
    --shared-openssl \
    --shared-zlib \
    --shared-brotli \
    --shared-cares
    # --shared-v8
    # --shared-http-parser

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

  rm -r "$pkgdir"/usr/{bin,lib/node_modules,share/doc,share/man}
}

# vim:set ts=2 sw=2 et:

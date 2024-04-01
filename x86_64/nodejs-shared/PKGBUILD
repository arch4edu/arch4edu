# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor  Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: James Campos <james.r.campos@gmail.com>
# Contributor: BlackEagle < ike DOT devolder AT gmail DOT com >
# Contributor: Dongsheng Cai <dongsheng at moodle dot com>
# Contributor: Masutu Subric <masutu.arch at googlemail dot com>
# Contributor: TIanyi Cui <tianyicui@gmail.com>

pkgbase=nodejs-shared
pkgname=(nodejs-shared libnode)
pkgver=21.7.1
pkgrel=3
pkgdesc='Evented I/O for V8 javascript'
arch=('x86_64')
url='https://nodejs.org/'
license=('MIT')
options=(!lto)
depends=('icu' 'libuv' 'libnghttp2' 'libnghttp3' 'libngtcp2' 'openssl' 'zlib' 'brotli' 'c-ares') # 'http-parser' 'v8')
makedepends=('git' 'python' 'procps-ng')
source=("nodejs-${pkgver}.tar.gz::https://github.com/nodejs/node/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('8d8c4d006c72315da80a52d15ea59c9cda3109bd58b086c3c5a153fa8af098c221cc3f3eb5bef287ad233195ab0ff728dfbbe14f0fed0f3c286479d63d29aab5')

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

#check() {
#  cd node-${pkgver}
#  make test || :
#}

package_nodejs-shared() {
  optdepends=('npm: nodejs package manager')
  provides=('nodejs' 'libnode')
  conflicts=('nodejs' 'libnode')

  cd node-${pkgver}
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"

  cd "$pkgdir"/usr/lib
  ln -s libnode.so.* libnode.so
}

package_libnode() {
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

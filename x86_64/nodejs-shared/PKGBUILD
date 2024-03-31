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
_commit=84c7e6fad4adbc972e0fecf537d6c6a3accf6b9e
pkgrel=2
pkgdesc='Evented I/O for V8 javascript'
arch=('x86_64')
url='https://nodejs.org/'
license=('MIT')
options=(!lto)
depends=('icu' 'libuv' 'libnghttp2' 'libnghttp3' 'libngtcp2' 'openssl' 'zlib' 'brotli' 'c-ares') # 'http-parser' 'v8')
makedepends=('git' 'python' 'procps-ng')
source=("node-${pkgver}.zip::https://github.com/nodejs/node/archive/${_commit}.zip")
sha512sums=('82699400af0ee082c6ff24560e3acfd99dd9e28f1701ad1ad1a41d8a925462b63cffa6a30b282e742c2ccc3a32fc13064f6d783feb5ed1282a95905532978c5a')

build() {
  cd node-${_commit}

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
#  cd node-${_commit}
#  make test || :
#}

package_nodejs-shared() {
  optdepends=('npm: nodejs package manager')
  provides=('nodejs')
  conflicts=('nodejs')

  cd node-${_commit}
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"

  cd "$pkgdir"/usr/lib
  ln -s libnode.so.* libnode.so
}

package_libnode() {
  cd node-${_commit}
  make DESTDIR="$pkgdir" install
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"

  cd "$pkgdir"/usr/lib
  ln -s libnode.so.* libnode.so

  rm -r "$pkgdir"/usr/{bin,include,lib/node_modules,share/doc,share/man}
}

# vim:set ts=2 sw=2 et:

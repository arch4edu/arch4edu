# Maintainer: Guillaume Horel <guillaume.horel@gmail.com>
# Contributor: Lukas Fleischer <lfleischer@archlinux.org>
# Contributor: Aleksey Filippov <sarum9in@gmail.com>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: Thomas S Hatch <thatch45@gmail.com>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname='protobuf-static'
_pkgname='protobuf'
pkgver=3.15.8
pkgrel=1
pkgdesc="Protocol Buffers - Google's data interchange format"
arch=('x86_64')
url='https://developers.google.com/protocol-buffers/'
license=('BSD')
depends=('gcc-libs' 'zlib')
makedepends=()
options=('staticlibs')
provides=("protobuf=$pkgver")
conflicts=('protobuf')
source=("$_pkgname-$pkgver.tgz::https://github.com/google/${_pkgname}/archive/v${pkgver}.tar.gz"
    "no-thirdparty.patch")
sha256sums=('0cbdc9adda01f6d2facc65a22a2be5cecefbefe5a09e5382ee8879b522c04441'
            '6fc836196e69b872794e821111df64effe69f984d46d83c902a9df8953a868b3')

prepare() {
  cd "$_pkgname-$pkgver"
  rm -rf third_party
  patch -p1 < ../no-thirdparty.patch
}

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  autoreconf -vif
  ./configure --prefix=/usr
  make CFLAGS="$CFLAGS -fPIC" CXXFLAGS="$CXXFLAGS -fPIC"
}

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  make DESTDIR="$pkgdir" install

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 editors/protobuf-mode.el "$pkgdir"/usr/share/emacs/site-lisp/protobuf-mode.el
}

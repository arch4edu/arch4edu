# Maintainer: acxz <akashpatel2008 at yaoo dot com>
# Contributor: Joe Neeman <joeneeman@gmail.com>
# Contributor: Rémy Oudompheng <oudomphe@clipper.ens.fr>
# Contributor: Alessandro "jakedust" Andrioni <jakedust@gmail.com>
pkgname=mpir
pkgver=3.0.0
pkgrel=3
pkgdesc="Library for multiple precision integers and rationals"
arch=('i686' 'x86_64' 'aarch64')
url="https://www.mpir.org/"
license=('LGPL')
depends=('gcc-libs')
makedepends=('yasm')
source=("$pkgname-$pkgver.tar.gz::https://www.github.com/wbhart/mpir/archive/refs/tags/mpir-$pkgver.tar.gz"
        "get_d.patch::https://patch-diff.githubusercontent.com/raw/wbhart/mpir/pull/296.patch")
sha256sums=('86a5039badc3e6738219a262873a1db5513405e15ece9527b718fcd0fac09bb2'
            'SKIP')
install=mpir.install

prepare() {
  cd "$srcdir/mpir-mpir-$pkgver"
  patch -Np1 < "${srcdir}/get_d.patch"
}

build() {
  cd "$srcdir/mpir-mpir-$pkgver"
  [[ "$CARCH" == "i686" ]] && export ABI=32
  ./autogen.sh
  ./configure --prefix=/usr --enable-cxx
  make
}

package() {
  cd "$srcdir/mpir-mpir-$pkgver"
  make DESTDIR="$pkgdir" install
}


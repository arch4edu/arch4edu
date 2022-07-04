# Maintainer: Martchus <martchus@gmx.net>
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>

pkgname=pocketsphinx
pkgver=5prealpha
pkgrel=13
pkgdesc='Lightweight speech recognition engine'
arch=('i686' 'x86_64')
url='http://cmusphinx.sourceforge.net'
license=('BSD')
makedepends=('swig' 'python')
depends=('sphinxbase=5prealpha' 'gst-plugins-base-libs')
source=("https://downloads.sourceforge.net/cmusphinx/$pkgname-$pkgver.tar.gz")
sha256sums=('ef5bb5547e2712bdf571f256490ef42a47962033892efd9d7df8eed7fe573ed9')
options=('!libtool')

prepare() {
  cd "$pkgname-$pkgver"

  echo "Reconfiguring project for current version of Automake"
  autoreconf -ivf > /dev/null
}

build() {
  cd "$pkgname-$pkgver"

  export PYTHON=/usr/bin/python PYTHONWARNINGS=ignore
  ./configure --prefix=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make DESTDIR="$pkgdir" install

  install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
  install -D -m644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

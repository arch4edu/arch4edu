# Maintainer: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>
# Contributor: Martchus <martchus@gmx.net>

pkgname=pocketsphinx
pkgver=5prealpha
pkgrel=9
pkgdesc='Lightweight speech recognition engine, specifically tuned for handheld and mobile devices, though it works equally well on the desktop.'
arch=('i686' 'x86_64')
url='http://cmusphinx.sourceforge.net'
license=('BSD')
makedepends=('swig' 'python2' 'python')
depends=('sphinxbase=5prealpha' 'gst-plugins-base-libs')
source=("http://downloads.sourceforge.net/cmusphinx/$pkgname-$pkgver.tar.gz")
sha256sums=('ef5bb5547e2712bdf571f256490ef42a47962033892efd9d7df8eed7fe573ed9')
options=('!libtool')

prepare() {
  cd "$pkgname-$pkgver"

  msg2 "Reconfiguring project for current version of Automake"
  autoreconf -ivf > /dev/null

  cd ..

  cp -R "$pkgname-$pkgver" "$pkgname-$pkgver-py2"
  cp -R "$pkgname-$pkgver" "$pkgname-$pkgver-py3"
}

build() {

  msg2 "Building python3 environment"
  export PYTHON=/usr/bin/python
  cd "$pkgname-$pkgver-py3"
  ./configure --prefix=/usr
  make


  msg2 "Building python2 environment"
	cd "../$pkgname-$pkgver-py2"
	export PYTHON=/usr/bin/python2
  ./configure --prefix=/usr
	make
}

package() {
	cd "$pkgname-$pkgver-py3"

	make DESTDIR="$pkgdir" install

  cd "../$pkgname-$pkgver-py2/swig"
  make DESTDIR="$pkgdir" install

	install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}"
	install -D -m644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  libtool --finish "$pkgdir/usr/lib"
  libtool --finish "$pkgdir/usr/lib/gstreamer-1.0"
  libtool --finish "$pkgdir/usr/lib/python2.7/site-packages/pocketsphinx"
  libtool --finish "$pkgdir/usr/lib/python3.6/site-packages/pocketsphinx"
}

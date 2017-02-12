# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
pkgname=xrootd-abi0
_pkgname=xrootd
pkgver=4.6.0
pkgrel=1
pkgdesc="A project that aims at giving high performance, scalable fault tolerant access to data repositories of many kinds."
provides=('xrootd'
          'xrootd-abi0')
conflicts=('xrootd')
arch=('i686' 'x86_64')
url="http://xrootd.org/"
license=('LGPL3')
depends=('ceph'
'libxml2'
)
makedepends=('make' 'cmake')
options=('!emptydirs')

source=(
	"http://xrootd.org/download/v$pkgver/xrootd-$pkgver.tar.gz"
)

sha256sums=('b50f7c64ed2a4aead987de3fdf6fce7ee082407ba9297b6851cd917db72edd1d')
build() {
	cd "$srcdir"

	rm -rf "build"
	mkdir "build"
	cd "build"

	cmake "$srcdir/$_pkgname-$pkgver" \
	-DCMAKE_BUILD_TYPE:STRING=Release \
        -DCMAKE_INSTALL_LIBDIR:PATH=lib -DCMAKE_INSTALL_PREFIX:PATH=/usr || return 1
	make ${MAKEFLAGS} || return 2
}

package() {
	cd "$srcdir/build"
	make DESTDIR="$pkgdir/" install
}

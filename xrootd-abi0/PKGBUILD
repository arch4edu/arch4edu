# Maintainer: Konstantin Gizdov < arch at kge dot pw >
# Contributor: Jan Kašpar < jan.kaspar at gmail dot com >
pkgname=xrootd-abi0
_pkgname=xrootd
pkgver=4.5.0
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

source=(
	"http://xrootd.org/download/v$pkgver/xrootd-$pkgver.tar.gz"
)

sha256sums=('27a8e4ef1e6bb6bfe076fef50afe474870edd198699d43359ef01de2f446c670')
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

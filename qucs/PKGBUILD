# Maintainer: Nils Czernia <nils[at]czserver.de>
# Contributor: Víctor Martínez Romanos <vmromanos@gmail.com>

pkgname=qucs
pkgver=0.0.20_rc2
_pkgver=0.0.20
pkgrel=2
pkgdesc="An integrated circuit simulator with a graphical user interface"
arch=('x86_64')
url="http://qucs.sourceforge.net"
license=('GPL')
depends=('gcc-libs' 'qt4' 'adms')
makedepends=('gperf')
optdepends=('freehdl: to permit digital circuit simulation'
#	    'asco: to enable circuit optimization'
	    'perl')
source=("http://downloads.sourceforge.net/project/qucs/qucs/${pkgver%_*}/qucs-${pkgver//_/-}.tar.gz")
sha256sums=('66cfa0b9f8baa8468feb81b3a15f165e1946511893fa9cfee7009167daa04d19')

build() {
  cd "$srcdir"/$pkgname-${_pkgver}
  ./configure --prefix=/usr --disable-doc
  make RCC=/usr/bin/rcc-qt4
}

package() {
  cd "$srcdir"/$pkgname-${_pkgver}
  make DESTDIR="$pkgdir" install
}

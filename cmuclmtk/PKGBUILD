# Maintainer: Your Name <youremail@domain.com>
pkgname=cmuclmtk
pkgver=0.7
pkgrel=1
epoch=
pkgdesc="Language model tools for CMU Sphinx"
arch=('i686' 'x86_64')
url="http://cmusphinx.sourceforge.net"
license=('BSD')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=(http://downloads.sourceforge.net/cmusphinx/$pkgname-$pkgver.tar.gz)
noextract=()
md5sums=('21bfb116d309e43e61def3692f98cdac')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  make DESTDIR="$pkgdir/" install
}

# vim:set ts=2 sw=2 et:

# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: aimileus <me at aimileus dot nl>
# Contributor: Salvador Pardiñas <darkfm@vera.com.uy>

pkgname=woeusb
pkgver=3.3.0
pkgrel=1
pkgdesc="A Linux program to create Windows USB stick installer from a real Windows DVD or an image"
arch=('x86_64')
url="https://github.com/slacka/WoeUSB"
license=('GPL3')
depends=('wxgtk2' 'grub' 'dosfstools' 'parted' 'wget' 'ntfs-3g')
optdepends=('gksu')
conflicts=('woeusb-git')
provides=('woeusb-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/slacka/WoeUSB/archive/v$pkgver.tar.gz")
sha256sums=('dc0e1a233143a33182339915d043a419c089b8bfb0d3813b17acbff2bdb285bb')

prepare() {
	cd "WoeUSB-$pkgver"
	autoreconf --install
	./configure --prefix=/usr
}

build() {
	cd "WoeUSB-$pkgver"
	make
}

package() {
	cd "WoeUSB-$pkgver"
	make DESTDIR="$pkgdir/" install
}


# Maintainer: aimileus <me at aimileus dot nl>
# Contributor: Salvador Pardiñas <darkfm@vera.com.uy>
pkgname=woeusb
pkgver=3.2.12
pkgrel=1
pkgdesc="A Linux program to create Windows USB stick installer from a real Windows DVD or an image"
arch=('x86_64')
url="https://github.com/slacka/WoeUSB"
license=('GPL3')
depends=('wxgtk2' 'grub' 'dosfstools' 'parted' 'wget' 'ntfs-3g')
optdepends=('gksu')
makedepends=('git')
conflicts=('woeusb-git')
provides=('woeusb-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/slacka/WoeUSB/archive/v$pkgver.tar.gz")
sha256sums=('a70226893fa99a0f7fb00609d54f6a2b1d27c4f2c5e12b612cdbe5735a5053f4')

prepare() {
	cd "WoeUSB-$pkgver"
	autoreconf --install
}

build() {
	cd "WoeUSB-$pkgver"
	./configure --prefix=/usr
	make
}

package() {
	cd "WoeUSB-$pkgver"
	make DESTDIR="$pkgdir/" install
}


# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: aimileus <me at aimileus dot nl>
# Contributor: Salvador Pardiñas <darkfm@vera.com.uy>

pkgname=woeusb
pkgver=3.3.0
pkgrel=2
pkgdesc="A Linux program to create Windows USB stick installer from a Windows DVD or an image"
arch=('x86_64')
url="https://github.com/slacka/WoeUSB"
license=('GPL3')
depends=('wxgtk2' 'grub' 'dosfstools' 'parted' 'wget' 'ntfs-3g')
optdepends=('gksu')
conflicts=('woeusb-git')
source=("$pkgname-$pkgver.tar.gz::https://github.com/slacka/WoeUSB/archive/v$pkgver.tar.gz"
        "disable_writeback_workaround.patch")
sha256sums=('dc0e1a233143a33182339915d043a419c089b8bfb0d3813b17acbff2bdb285bb'
            'f051d9dbf1015596327b91abeea5c9f2404904e40e168f798fb4447e3fa9acb5')

prepare() {
	cd "WoeUSB-$pkgver"

	# Disable changing kernel cache behaviour, since it fails on newer versions
	# See https://github.com/slacka/WoeUSB/issues/267
	patch -Np1 -i "${srcdir}/disable_writeback_workaround.patch"

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


# Maintainer: Giovanni Harting <539@idlegandalf.com>
# Contributor: aimileus <me at aimileus dot nl>
# Contributor: Salvador Pardiñas <darkfm@vera.com.uy>

pkgname=woeusb
pkgver=3.3.1
pkgrel=1
pkgdesc="A Linux program to create Windows USB stick installer from a Windows DVD or an image"
arch=('x86_64')
url="https://github.com/slacka/WoeUSB"
license=('GPL3')
depends=('wxgtk2' 'grub' 'dosfstools' 'parted' 'wget' 'ntfs-3g')
makedepends=('git')
optdepends=('gksu')
conflicts=('woeusb-git')
source=("WoeUSB-${pkgver}::git+https://github.com/slacka/WoeUSB.git#tag=v${pkgver}")
sha256sums=('SKIP')

prepare() {
    cd "WoeUSB-$pkgver"

    grep 'filter=version' .gitattributes | cut -d' ' -f1 | while read file; do
        sed -i "s/@@WOEUSB_VERSION@@/${pkgver}/" $file
    done

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


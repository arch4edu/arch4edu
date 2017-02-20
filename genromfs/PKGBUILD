# Maintainer: Douglas RAILLARD <douglas dot raillard at gmail dot com>
# Contributor: jordz <jordz@archlinux.us>

pkgname=genromfs
pkgver=0.5.2
pkgrel=2
pkgdesc="tool for creating romfs images"
arch=(i686 x86_64)
url="http://romfs.sourceforge.net"
license=('GPL')
depends=(glibc)
source=(http://downloads.sourceforge.net/project/romfs/$pkgname/$pkgver/$pkgname-$pkgver.tar.gz)
md5sums=('2a91463c56f9e042edc330c063a0cf5a')

build() {
    cd "$pkgname-$pkgver"
    make
} 

package() {
    cd "$pkgname-$pkgver"
    
    # The provided install target does not install man page in correct folder: make PREFIX="$pkgdir" install
    mkdir -p "$pkgdir/usr/bin"
    install -m 755 genromfs "$pkgdir/usr/bin"
    
    mkdir -p "$pkgdir/usr/share/man/man8"
    gzip -f genromfs.8
    install -m 644 genromfs.8.gz "$pkgdir/usr/share/man/man8"
} 

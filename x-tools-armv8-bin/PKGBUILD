# Maintainer: JKA Network (JoseluCross, Kprkpr, Yukialba) <contacto@jkanetwork.com>
pkgname=x-tools-armv8-bin
pkgver=20170116
pkgrel=1
pkgdesc="crosstool-ng toolchain - x-tools package for armv8 compiling"
arch=('x86_64')
url="https://archlinuxarm.org/wiki/Distcc_Cross-Compiling"
license=('GPL3')
provides=('x-tools-armv8')
depends=('xz')
options=(!emptydirs)
source=('https://archlinuxarm.org/builder/xtools/x-tools8.tar.xz')
md5sums=('SKIP')
install=$pkgname.install
noextract=('x-tools8.tar.xz')
package() {
	mkdir -p "$pkgdir/usr/x-tools"
	tar -Jxf "$srcdir/x-tools8.tar.xz" -C "$pkgdir/usr/x-tools" 
}

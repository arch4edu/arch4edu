# Maintainer: JKA Network (JoseluCross, Kprkpr, Yukialba) <contacto@jkanetwork.com>
pkgname=x-tools-armv7-bin
pkgver=7.3.1
pkgrel=1
pkgdesc="crosstool-ng toolchain - x-tools package for armv7h compiling"
arch=('x86_64')
url="https://archlinuxarm.org/wiki/Distcc_Cross-Compiling"
license=('GPL3')
provides=('x-tools-armv7')
depends=('xz')
options=(!emptydirs)
source=("https://archlinuxarm.org/builder/xtools/${pkgver}-1/x-tools7h.tar.xz")
md5sums=('f8bf79552382e926c5d474c6cde0639a')
install=$pkgname.install
noextract=('x-tools7h.tar.xz')
package() {
	mkdir -p "$pkgdir/usr/x-tools"
	tar -Jxf "$srcdir/x-tools7h.tar.xz" -C "$pkgdir/usr/x-tools" 
}

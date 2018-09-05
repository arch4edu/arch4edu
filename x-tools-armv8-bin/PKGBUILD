# Maintainer: JKA Network (JoseluCross, Kprkpr, Yukialba) <contacto@jkanetwork.com>
pkgname=x-tools-armv8-bin
pkgver=8.2.0
pkgrel=1
pkgdesc="crosstool-ng toolchain - x-tools package for armv8 compiling"
arch=('x86_64')
url="https://archlinuxarm.org/wiki/Distcc_Cross-Compiling"
license=('GPL3')
provides=('x-tools-armv8')
depends=('xz')
options=(!emptydirs)
source=("https://archlinuxarm.org/builder/xtools/${pkgver}-1/x-tools8.tar.xz")
md5sums=('72a1c898aba9f27b9234507d326bdaa9')
install=$pkgname.install
noextract=('x-tools8.tar.xz')
package() {
	mkdir -p "$pkgdir/opt/x-tools"
	tar -Jxf "$srcdir/x-tools8.tar.xz" -C "$pkgdir/opt/x-tools" 
}

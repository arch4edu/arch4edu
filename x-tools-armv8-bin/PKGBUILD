# Maintainer: JKA Network (JoseluCross, Kprkpr, Yukialba) <contacto@jkanetwork.com>
pkgname=x-tools-armv8-bin
pkgver=8.2.0
pkgrel=2
pkgdesc="crosstool-ng toolchain - x-tools package for armv8 compiling"
arch=('x86_64')
url="https://archlinuxarm.org/wiki/Distcc_Cross-Compiling"
license=('GPL3')
provides=('x-tools-armv8')
depends=('xz')
options=(!emptydirs)
source=("https://archlinuxarm.org/builder/xtools/${pkgver}-${pkgrel}/x-tools8.tar.xz")
md5sums=('0243bc25f569b1813481efe0637c872c')
install=$pkgname.install
noextract=('x-tools8.tar.xz')
package() {
	mkdir -p "$pkgdir/opt/x-tools"
	tar -Jxf "$srcdir/x-tools8.tar.xz" -C "$pkgdir/opt/x-tools" 
}

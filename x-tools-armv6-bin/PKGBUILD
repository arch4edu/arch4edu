# Maintainer: JKA Network (JoseluCross, Kprkpr, Yukialba) <contacto@jkanetwork.com>
pkgname=x-tools-armv6-bin
pkgver=8.2.1
pkgrel=1
pkgdesc="crosstool-ng toolchain - x-tools package for armv6h compiling"
arch=('x86_64')
url="https://archlinuxarm.org/wiki/Distcc_Cross-Compiling"
license=('GPL3')
provides=('x-tools-armv6')
depends=('xz')
options=(!emptydirs)
source=("https://archlinuxarm.org/builder/xtools/${pkgver}-1/x-tools6h.tar.xz")
md5sums=('6bf18a8130b5de2a8b9f7fbf047d9f8f')
install=$pkgname.install
noextract=('x-tools6h.tar.xz')
package() {
	mkdir -p "$pkgdir/opt/x-tools"
	tar -Jxf "$srcdir/x-tools6h.tar.xz" -C "$pkgdir/opt/x-tools" 
}

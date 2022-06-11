# Maintainer: Katherine J. Cumberbatch <stykers@stykers.moe>
pkgname=binfmt-qemu-static
pkgver=20210119
pkgrel=1
pkgdesc="Register qemu-static interpreters for various binary formats"
arch=('any')
url="http://www.freedesktop.org/software/systemd/man/binfmt.d.html"
license=('GPL')
optdepends=('qemu-user-static')
source=("qemu-static.conf")
md5sums=('4ce74ae99d838f46898ff3222a998d8b')

package() {
  install -Dm 644 "$srcdir/qemu-static.conf" "$pkgdir/usr/lib/binfmt.d/qemu-static.conf"
}

# vim:set ts=2 sw=2 et:

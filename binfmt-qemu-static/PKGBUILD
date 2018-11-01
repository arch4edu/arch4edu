# Maintainer: Jonathan Liu <net147@gmail.com>
pkgname=binfmt-qemu-static
pkgver=20160602
pkgrel=2
pkgdesc="Register qemu-static interpreters for various binary formats"
arch=('any')
url="http://www.freedesktop.org/software/systemd/man/binfmt.d.html"
license=('GPL')
optdepends=('qemu-user-static')
source=("qemu-static.conf")
md5sums=('aafb4b804b6f5b16ac3aebe5d199769b')

package() {
  install -Dm 644 "$srcdir/qemu-static.conf" "$pkgdir/usr/lib/binfmt.d/qemu-static.conf"
}

# vim:set ts=2 sw=2 et:

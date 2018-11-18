# Maintainer: Bailey Kasin <bailey@gingertechnology.net>
pkgname=binfmt-qemu-static
pkgver=20181118
pkgrel=3
pkgdesc="Register qemu-static interpreters for various binary formats"
arch=('any')
url="http://www.freedesktop.org/software/systemd/man/binfmt.d.html"
license=('GPL')
optdepends=('qemu-user-static')
source=("qemu-static.conf")
md5sums=('16d2fdf5cbd499b3c3e7c2fd0b75bc20')

package() {
  install -Dm 644 "$srcdir/qemu-static.conf" "$pkgdir/usr/lib/binfmt.d/qemu-static.conf"
}

# vim:set ts=2 sw=2 et:

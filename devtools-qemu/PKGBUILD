pkgname=devtools-qemu
pkgver=2.76715c0
pkgrel=1
pkgdesc='QEMU based cross-build tools for Archlinux package maintainers'
arch=('x86_64')
url='http://github.com/petronny/devtools-qemu'
license=('GPL')
depends=('binfmt-qemu-static' 'devtools-alarm' 'qemu-user-static-bin')
makedepends=('git')
source=('git://github.com/petronny/devtools-qemu.git')
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  echo "$(git rev-list --count master).$(git rev-parse --short master)"
}

build() {
  cd $srcdir/$pkgname

  cp /usr/bin/archbuild qemu_archbuild
  patch qemu_archbuild < qemu.patch
}

package() {
  mkdir -p $pkgdir/usr/bin
  mkdir -p $pkgdir/usr/share/devtools

  cp $srcdir/$pkgname/qemu_archbuild $pkgdir/usr/bin
  cp $srcdir/$pkgname/mirrorlist $pkgdir/usr/share/devtools/qemu_mirrorlist

  for i in armv6h armv7h aarch64
  do
    cp $srcdir/$pkgname/pacman-extra-$i.conf $pkgdir/usr/share/devtools/
    cp $srcdir/$pkgname/makepkg-$i.conf $pkgdir/usr/share/devtools/
    ln -sf /usr/bin/qemu_archbuild $pkgdir/usr/bin/extra-$i-build
  done
}

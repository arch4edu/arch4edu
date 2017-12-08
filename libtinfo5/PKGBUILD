# Maintainer: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Alexej Magura <sickhadas.nix*gmail*>

pkgname=libtinfo5
pkgver=5
pkgrel=18
pkgdesc="symlink to ncurses for use in cuda and other packages (legacy)"
arch=('any')
url="http://www.gnu.org/software/ncurses/"
license=('MIT')
depends=('ncurses')

package() {
  install -d "${pkgdir}/usr/lib"
  ln -s "/usr/lib/libncursesw.so.6.0" -T "${pkgdir}/usr/lib/libtinfo.so.5"
}

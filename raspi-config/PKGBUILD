# Maintainer: Jefferson Gonzalez <jgmdev@gmail.com>

pkgname=raspi-config
pkgver=r2.aa2dfd1
pkgrel=1
pkgdesc="Raspberry pi raspi-config utility adapted for ArchLinux ARM."
arch=('armv6h' 'armv7h' 'aarch64')
url="https://github.com/jgmdev/alarm-raspi-config"
license=('MIT')
depends=('xorg-xrandr' 'libnewt')
provides=('raspi-config')
source=("git://github.com/jgmdev/alarm-raspi-config.git")
md5sums=('SKIP')
_gitname=alarm-raspi-config

pkgver() {
  cd "${srcdir}/${_gitname}"
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" \
      "$(git rev-list --count HEAD)" \
      "$(git log | head -n 1 | cut -d" " -f2 | awk '{print substr($0,0,7)}')"
  )
}

package() {
  cd "${srcdir}/$_gitname"

  make DESTDIR="${pkgdir}" install
}

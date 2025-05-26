# Maintainer: w0rty <mawo97 at gmail.com>
# Maintainer: Mr.Wizard <arch.aur-emailme at yahoo.com>
# Contributor: 4679 <admin@libnull.com>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Allan McRae <allan@archlinux.org>
# Contributor: Jochem Kossen <j.kossen@home.nl>

pkgname=fakeroot-tcp
_pkgname=fakeroot
pkgver=1.37.1.2
pkgrel=1
pkgdesc='Tool for simulating superuser privileges,with tcp ipc'
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
license=('GPL')
url='https://tracker.debian.org/pkg/fakeroot'
install=fakeroot.install
depends=('glibc' 'filesystem' 'sed' 'util-linux' 'sh')
makedepends=('po4a' 'automake' 'autoconf')
provides=("${_pkgname}=${pkgver}-${pkgrel}")
conflicts=("${_pkgname}")
source=(http://ftp.debian.org/debian/pool/main/f/$_pkgname/${_pkgname}_${pkgver}.orig.tar.gz)
sha256sums=('959496928c8a676ec8377f665ff6a19a707bfad693325f9cc4a4126642f53224')


prepare() {
  cd $_pkgname-$pkgver
}

build() {
  cd $_pkgname-$pkgver

  ./bootstrap
  ./configure --prefix=/usr \
    --libdir=/usr/lib/libfakeroot \
    --disable-static \
    --with-ipc=tcp

  make

  cd doc
  po4a -k 0 --rm-backups --variable "srcdir=../doc/" po4a/po4a.cfg
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install

  install -dm755 "$pkgdir"/etc/ld.so.conf.d/
  echo '/usr/lib/libfakeroot' > "$pkgdir"/etc/ld.so.conf.d/fakeroot.conf

  # install README for sysv/tcp usage
  install -Dm644 README "$pkgdir"/usr/share/doc/$_pkgname/README
}


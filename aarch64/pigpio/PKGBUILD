# Maintainer:
# Contributor: Christopher Arndt <aur -at- chrisarndt -dot- de>

## useful links
# http://abyz.me.uk/rpi/pigpio/
# https://github.com/joan2937/pigpio

_pkgname=pigpio
pkgname="$_pkgname"
pkgver=79
pkgrel=3
pkgdesc='A library for C and Python with system service for controlling GPIOs on a Raspberry Pi'
url='http://abyz.me.uk/rpi/pigpio/'
license=('Unlicense')
arch=('x86_64' 'aarch64' 'armv7h')

depends=('python')
makedepends=('python-setuptools')

provides=(
  "python-$pkgname"
  'libpigpio.so'
)
conflicts=("python-$pkgname")

_pkgsrc="$pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"https://github.com/joan2937/pigpio/archive/v$pkgver.tar.gz")
sha256sums=('c5337c0b7ae888caf0262a6f476af0e2ab67065f7650148a0b21900b8d1eaed7')

prepare() {
  cd "$_pkgsrc"
  sed -e 's/ -lrt//' \
    -e 's/-Wl/\$(LDFLAGS)/' \
    -e 's/\$(CC) -o/\$(CC) $(LDFLAGS) -o/' \
    -e '/which python2/d' \
    -e '/\/opt/d' \
    -e 's|\$(prefix)/man|\$(prefix)/share/man|' \
    -i Makefile

  sed -e 's|/usr/bin/pigpiod|/usr/bin/pigpiod -k|' -i util/pigpiod.service
}

build() {
  cd "$_pkgsrc"
  make
}

package() {
  cd "$_pkgsrc"
  make prefix=/usr DESTDIR="$pkgdir" install
  install -Dm644 util/pigpiod.service -t "$pkgdir"/usr/lib/systemd/system
}

# $Id$
# Maintainer: Sergej Pupykin <arch+pub@sergej.pp.ru>

pkgname=adms
pkgver=2.3.7
pkgrel=1
pkgdesc="codegenerator for the VERILOG-A(MS) language"
arch=('x86_64' 'i686')
url="https://github.com/qucs/adms"
license=('GPL')
depends=('glibc')
makedepends=('git' 'autoconf' 'automake' 'flex' 'bison' 'perl-gd' 'perl-xml-libxml')
options=(!makeflags)
source=("$pkgname-$pkgver.tar.gz::https://github.com/Qucs/ADMS/archive/release-$pkgver.tar.gz")
sha256sums=('0d24f645d7ce0daa447af1b0cff1123047f3b73cc41cf403650f469721f95173')

build() {
  cd ADMS-release-$pkgver
  ./bootstrap.sh
  ./configure --enable-maintainer-mode --prefix=/usr
  # Fight unused direct deps
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/    if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/      func_append compile_command " -Wl,-O1,--as-needed"\n      func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool
  make
}

package() {
  cd ADMS-release-$pkgver
  make DESTDIR="$pkgdir" install
}

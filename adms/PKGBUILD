# $Id$
# Maintainer: Sergej Pupykin <arch+pub@sergej.pp.ru>

pkgname=adms
pkgver=2.3.6
pkgrel=1
pkgdesc="ADMS is a codegenerator for the VERILOG-A(MS) language"
arch=('x86_64')
url="https://github.com/qucs/adms"
license=('GPL')
depends=('glibc')
makedepends=('git' 'autoconf' 'automake' 'flex' 'bison' 'perl-gd' 'perl-xml-libxml')
options=(!makeflags)
source=("$pkgname-$pkgver.tar.gz::https://github.com/Qucs/ADMS/archive/release-$pkgver.tar.gz")
sha256sums=('aaf3f635aae41e1c11913e09b8e1bc5eea64256dcec70f3f60d1b9a794af6053')

build() {
  cd ADMS-release-$pkgver
  ./bootstrap.sh
  ./configure --enable-maintainer-mode --prefix=/usr
  make
}

package() {
  cd ADMS-release-$pkgver
  make DESTDIR="$pkgdir" install
}

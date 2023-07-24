# Maintainer:  Anton Kudelin <kudelin at protonmail dot com>
# Contributor: xiretza <xiretza+aur@gmail.com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Jesin <jesin00@gmail.com>
# Contributor: Gabriele Lanaro <gabriele.lanaro@gmail.com>

pkgname=f2c
pkgver=20230428
pkgrel=1
pkgdesc='Fortran to C code translator'
url='https://www.netlib.org/f2c'
license=(custom)
arch=(x86_64 aarch64)
depends=(glibc)
makedepends=(unzip)
source=($pkgname-$pkgver.tar.gz::$url/src.tgz
        lib$pkgname-$pkgver.zip::$url/libf2c.zip)
noextract=(libf2c.zip)
sha256sums=('74ba67c321a3b629216c7ed5a48a061c3e5c3722ac85ceb01dcce6913751705a'
            'ca404070e9ce0a9aaa6a71fc7d5489d014ade952c5d6de7efb88de8e24f2e8e0')

prepare() {
  cd "$srcdir"
  mv src $pkgname-$pkgver
  mkdir lib$pkgname
  unzip -q lib$pkgname-$pkgver.zip -d lib$pkgname-$pkgver
  sed -i "s@-O@-O -ansi -fPIC@g" lib$pkgname-$pkgver/makefile.u
  sed -i "/MAIN__/d" lib$pkgname-$pkgver/main.c
}

build() {
  cd "$srcdir/lib$pkgname-$pkgver"
  make hadd -f makefile.u
  make -f makefile.u
  make -f makefile.u libf2c.so
  
  cd "$srcdir/$pkgname-$pkgver"
  make -f makefile.u
}

package() {
  cd "$pkgdir"
  install -dm755 usr/{bin,include,lib,share/{licenses/$pkgname,man/man1}}
  install -m755 "$srcdir/$pkgname-$pkgver/f2c" usr/bin
  install -m755 "$srcdir/lib$pkgname-$pkgver/libf2c.so" usr/lib
  install -m755 "$srcdir/lib$pkgname-$pkgver/f2c.h" usr/include
  install -m755 "$srcdir/$pkgname-$pkgver/f2c.1t" usr/share/man/man1/f2c.1
  cat <<EOF > usr/share/licenses/$pkgname/LICENSE
Copyright 1990-1996, 2000-2001 by AT&T, Lucent Technologies and Bellcore.

Permission to use, copy, modify, and distribute this software
and its documentation for any purpose and without fee is hereby
granted, provided that the above copyright notice appear in all
copies and that both that the copyright notice and this
permission notice and warranty disclaimer appear in supporting
documentation, and that the names of AT&T, Bell Laboratories,
Lucent or Bellcore or any of their entities not be used in
advertising or publicity pertaining to distribution of the
software without specific, written prior permission.

AT&T, Lucent and Bellcore disclaim all warranties with regard to
this software, including all implied warranties of
merchantability and fitness.  In no event shall AT&T, Lucent or
Bellcore be liable for any special, indirect or consequential
damages or any damages whatsoever resulting from loss of use,
data or profits, whether in an action of contract, negligence or
other tortious action, arising out of or in connection with the
use or performance of this software.
EOF
}

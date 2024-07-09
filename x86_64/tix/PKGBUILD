# Maintainer: Dante Melhado <dmelhado@dc.uba.ar>
# Contributor: Brian Bidulock <bidulock@openss7.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Brice Méalier <mealier_brice@yahoo.fr>

pkgname=tix
pkgver=8.4.3
pkgrel=7
pkgdesc="Tk Interface eXtension, a powerful set of user interface components"
arch=('x86_64' 'i686')
url="http://tix.sourceforge.net/"
license=("BSD")
depends=('tk' 'libx11')
source=(
  "http://downloads.sourceforge.net/tix/Tix$pkgver-src.tar.gz"
  "tix-$pkgver-tcl8.5.patch::https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-tcltk/tix/files/tix-$pkgver-tcl8.5.patch"
  "tix-$pkgver-tcl8.6.patch::https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-tcltk/tix/files/tix-$pkgver-tcl8.6.patch"
  "tix-$pkgver-wimplicit-int.patch::https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-tcltk/tix/files/tix-$pkgver-wimplicit-int.patch"
  "tix-$pkgver-clang6.patch::https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-tcltk/tix/files/tix-$pkgver-clang6.patch"
  "tix-$pkgver-noopt.patch::https://gitweb.gentoo.org/repo/gentoo.git/plain/dev-tcltk/tix/files/tix-$pkgver-noopt.patch"
)
md5sums=(
  '2b8bf4b10a852264678182652f477e59'
  '874299ff5e6544fb4501ce23102a4148'
  'c26297f9e1744dc38308a062ef00549e'
  '9ebd0c46711d2eb3a8da500975c5f078'
  '7c7cb58bc019a8a1d8aa326f6eb323f7'
  'ff69e046a457955bd3aae4c09ea62f71'
)

prepare() {
  cd "$srcdir"/Tix$pkgver
  sed -i -e 's:-Os::g' -i configure tclconfig/tcl.m4
  for patch_file in "${srcdir}"/*.patch; do
    patch -Np1 -i "${patch_file}"
  done
  sed -i -e 's:generic/tclInt.h:tclInt.h:g' configure
  sed -i -e 's:generic/tkInt.h:tkInt.h:g' configure
}

build() {
  cd "$srcdir"/Tix$pkgver

  export CFLAGS="$CFLAGS -DERR_IN_PROGRESS=2"
  [[ $CARCH == "x86_64" ]] && BIT="--enable-64bit"

  ./configure --prefix=/usr \
    --with-tcl=/usr/lib \
    --with-tk=/usr/lib \
    $BIT

  make
}

package() {
  cd "$srcdir"/Tix$pkgver
  make DESTDIR="$pkgdir" install
  # move things around

  install -m755 tools/tixindex "$pkgdir"/usr/bin/tixindex
  rm -rf "$pkgdir"/usr/lib/Tix8.4/html
  rm -f "$pkgdir"/usr/lib/Tix8.4/{README.txt,license.terms}
  ln -s Tix$pkgver/libTix$pkgver.so "$pkgdir"/usr/lib/libTix$pkgver.so

  mkdir -p "$pkgdir"/usr/share/man/man1
  mkdir -p "$pkgdir"/usr/share/man/man3
  cp -p man/tixwish.1 "$pkgdir"/usr/share/man/man1
  cd "$srcdir"/Tix$pkgver/man
  for i in *.n; do
    cp -p $i "$pkgdir"/usr/share/man/man3/${i%n}3
  done

  mkdir -p "$pkgdir"/usr/share/licenses/tix
  cp "$srcdir"/Tix$pkgver/license.terms "$pkgdir"/usr/share/licenses/tix/
}

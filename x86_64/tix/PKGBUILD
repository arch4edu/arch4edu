# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Brice Méalier <mealier_brice@yahoo.fr>

pkgname=tix
pkgver=8.4.3
pkgrel=5
pkgdesc="Tk Interface eXtension, a powerful set of user interface components"
arch=('x86_64' 'i686')
url="http://tix.sourceforge.net/"
license=("BSD")
depends=('tk' 'libx11')
source=("http://downloads.sourceforge.net/tix/Tix$pkgver-src.tar.gz"
	"tix-8.4.3-tcl8.6.patch::https://bugs.archlinux.org/task/36882?getfile=10973"
	"tcl-tk-path.patch")
md5sums=('2b8bf4b10a852264678182652f477e59'
         'c26297f9e1744dc38308a062ef00549e'
         'd4df48da39dd51872d58706a51bab505')

prepare() {
  cd "$srcdir"/Tix$pkgver
  sed -i -e 's:-Os::g' -i configure tclconfig/tcl.m4
  patch -Np1 -i "${srcdir}/tix-8.4.3-tcl8.6.patch"
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
    $BIT \

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
  cp "$srcdir"/Tix$pkgver/license.terms  "$pkgdir"/usr/share/licenses/tix/
}

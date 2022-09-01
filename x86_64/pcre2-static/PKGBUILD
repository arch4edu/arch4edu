# Maintainer: crab2313 <crab2313@gmail.com>

pkgname=pcre2-static
pkgver=10.40
pkgrel=1
pkgdesc="A library that implements Perl 5-style regular expressions. 2nd version"
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url="http://www.pcre.org/"
license=('BSD')
depends=('gcc-libs')
options=('staticlibs' '!libtool')
validpgpkeys=('45F68D54BBE23FB3039B46E59766E084FB0F43D8')
source=("https://github.com/PhilipHazel/pcre2/releases/download/${pkgname%-static}-$pkgver/${pkgname%-static}-$pkgver.tar.bz2"{,.sig})

sha256sums=('14e4b83c4783933dc17e964318e6324f7cae1bc75d8f3c79bc6969f00c159d68'
            'SKIP')

build() {
  cd pcre2-$pkgver

  ./configure \
    --prefix=/usr \
    --enable-pcre2-16 \
    --enable-pcre2-32 \
    --enable-jit \
    --enable-pcre2grep-libz \
    --enable-pcre2grep-libbz2 \
    --enable-pcre2test-libreadline

  make
}

package() {
  cd "${srcdir}"/pcre2-${pkgver}
  make DESTDIR="${pkgdir}" install
  rm -rf $pkgdir/usr/{bin,include,share,lib/pkgconfig}
  rm -f $pkgdir/usr/lib/*.so*

  install -Dm644 LICENCE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}

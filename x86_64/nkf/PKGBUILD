# Contributor: noonov <noonov@gmail.com>

pkgname=nkf
pkgver=2.1.5
pkgrel=2
pkgdesc="A yet another kanji code converter among networks, hosts and terminals"
arch=('i686' 'x86_64')
url="https://osdn.net/projects/nkf/"
license=('custom')
depends=('glibc')
source=(https://osdn.net/dl/nkf/nkf-${pkgver}.tar.gz
        LICENSE)
md5sums=('2b8a0c455351ebdd9a622f48e7cab559'
         'f7d5e06e00b856f503e1dacc2ab86ad6')
b2sums=('b5ae8f51b0ed97261f9e82ad469adbc9e469e709dc5acb64bfba48881555931eade5fcb772e7956a7401399008ec33bd57c8d6d8b5790eefe4d69d4e1dabed7c'
        'b3738fe113b4f8bb27be883a6a4bef1ca209fe9e6ac9ab519bb6b5cef5154f7617d03ec6f52a8b94a83789a5eafaab14fc7364f54792784203d43ead6606b1d6')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  sed -i "/^CFLAGS/s|$| $CFLAGS|" Makefile
  make
  ./nkf -w --overwrite nkf.1j
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  install -D -m755 nkf               "${pkgdir}/usr/bin/nkf"
  install -D -m644 nkf.1             "${pkgdir}/usr/share/man/man1/nkf.1"
  install -D -m644 nkf.1j            "${pkgdir}/usr/share/man/ja/man1/nkf.1"
  install -D -m644 ${srcdir}/LICENSE "${pkgdir}/usr/share/licenses/nkf/LICENSE"
}

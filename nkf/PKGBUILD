# Contributor: noonov <noonov@gmail.com>

pkgname=nkf
pkgver=2.1.5
pkgrel=1
pkgdesc="A yet another kanji code converter among networks, hosts and terminals"
arch=('i686' 'x86_64')
url="http://sourceforge.jp/projects/nkf/"
license=('custom:zlib')
depends=('glibc')
source=(http://dl.sourceforge.jp/nkf/70406/${pkgname}-${pkgver}.tar.gz)
sha256sums=('d1a7df435847a79f2f33a92388bca1d90d1b837b1b56523dcafc4695165bad44')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}

  sed -i "/^CFLAGS/s|$| ${CFLAGS}|" Makefile

  make
  ./nkf -w --overwrite nkf.1j
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}

  install -D -m755 nkf    ${pkgdir}/usr/bin/nkf
  install -D -m644 nkf.1  ${pkgdir}/usr/share/man/man1/nkf.1
  install -D -m644 nkf.1j ${pkgdir}/usr/share/man/ja/man1/nkf.1
}

# Maintainer: r6eve <r6eve at acm dot org>
# Former Maintainer (thanks!) : noonov <noonov@gmail.com>
# Contributor: noonov <noonov@gmail.com>

pkgname=nkf
pkgver=2.1.5
pkgrel=3
pkgdesc="A yet another kanji code converter among networks, hosts and terminals"
arch=('i686' 'x86_64')
url="https://github.com/nurse/nkf"
license=('zlib')
depends=('glibc')
conflicts=("${pkgname}-git")
source=("${pkgname}-${pkgver}.tar.gz"::"${url}/archive/refs/tags/v${pkgver//./_}.tar.gz")
sha256sums=('10cf6eb3d4d095919185ac224d5a634e9926d731e656d04bacb270e5cae0e28c')

build() {
  cd ${srcdir}/${pkgname}-${pkgver//./_}
  make
  ./nkf -w --overwrite nkf.1j
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver//./_}
  install -D -m755 nkf    "${pkgdir}/usr/bin/nkf"
  install -D -m644 nkf.1  "${pkgdir}/usr/share/man/man1/nkf.1"
  install -D -m644 nkf.1j "${pkgdir}/usr/share/man/ja/man1/nkf.1"
}

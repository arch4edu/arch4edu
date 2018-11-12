# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: m4sk1n <m4sk1n@vivaldi.net>
# Contributor: CubeTheThird <cubethethird@gmail.com>
_pkgname=icu
pkgname=${_pkgname}58
pkgver=58.2
pkgrel=2
pkgdesc="International Components for Unicode library"
arch=('i686' 'x86_64')
url="http://www.icu-project.org/"
license=('custom:"icu"')
depends=('gcc-libs>=4.7.1-5')
source=(https://vorboss.dl.sourceforge.net/project/${_pkgname}/ICU4C/${pkgver}/${_pkgname}4c-${pkgver//./_}-src.tgz)
sha256sums=('2b0a4410153a9b20de0e20c7d8b66049a72aef244b53683d0d7521371683da0c')

prepare() {
    # fix xlocale.h problems (FS#55246)
    cd ${srcdir}/${_pkgname}/source
    sed -i 's/xlocale/locale/' i18n/digitlst.cpp
}

build() {
  cd ${srcdir}/${_pkgname}/source
  ./configure --prefix=/usr --sysconfdir=/etc --mandir=/usr/share/man
  make
}

package() {
  cd ${srcdir}/${_pkgname}/source
  make -j1 DESTDIR=${pkgdir} install
  rm -r "${pkgdir}"/usr/{bin,include,sbin,share,lib/*so,lib/icu/{Makefile.inc,current,pkgdata.inc}}
  rm -r "${pkgdir}/usr/lib/pkgconfig"

  # Install license
  install -Dm644 ${srcdir}/${_pkgname}/license.html ${pkgdir}/usr/share/licenses/${pkgname}/license.html
}

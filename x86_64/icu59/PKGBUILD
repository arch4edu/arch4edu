# Maintainer: Matt C <matt@xhec.us>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Author: CubeTheThird <cubethethird@gmail.com>

_pkgname=icu
pkgname=${_pkgname}59
pkgver=59.2
pkgrel=1
pkgdesc="International Components for Unicode library"
arch=('i686' 'x86_64')
url="http://www.icu-project.org/"
license=('custom:"icu"')
depends=('gcc-libs>=4.7.1-5')
source=(https://github.com/unicode-org/${_pkgname}/releases/download/release-${pkgver//./-}/icu4c-${pkgver//./_}-src.tgz)
sha256sums=('10741648470a0ed106d5f588cc51a03574254849b28bc1c42d4c2eec628d70cd')

prepare() {
    # fix xlocale.h problems (FS#55246)
    cd ${srcdir}/${_pkgname}/source
    sed -i 's/xlocale/locale/' i18n/digitlst.cpp
}

build() {
  cd ${srcdir}/${_pkgname}/source
  ./configure --prefix=/usr \
	--sysconfdir=/etc \
	--mandir=/usr/share/man
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

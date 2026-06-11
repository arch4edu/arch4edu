# Maintainer: Josh Ellithorpe <quest@mac.com>
# Contributor: Laurent Tréguier <laurent@treguier.org>

pkgname=lzfse
pkgver=1.0
pkgrel=5
_srcname="${pkgname}-${pkgname}-${pkgver}"
pkgdesc='LZFSE compression library and command line tool'
arch=('x86_64' 'aarch64')
url='https://github.com/lzfse/lzfse'
license=('BSD-3-Clause')
depends=('glibc')
conflicts=('lzfse-git')
options=('!strip')
source=("https://github.com/lzfse/lzfse/archive/lzfse-${pkgver}.tar.gz")
sha256sums=('cf85f373f09e9177c0b21dbfbb427efaedc02d035d2aade65eb58a3cbf9ad267')

build() {
    cd "${srcdir}/${_srcname}"
    sed -i 's/^CFLAGS[[:space:]]*:=/CFLAGS +=/' Makefile
    make
}

package() {
    install -Dm755 "${srcdir}/${_srcname}/build/bin/lzfse" "${pkgdir}/usr/bin/lzfse"
    install -Dm644 "${srcdir}/${_srcname}/src/lzfse.h" "${pkgdir}/usr/include/lzfse.h"
    install -Dm644 "${srcdir}/${_srcname}/build/bin/liblzfse.a" "${pkgdir}/usr/lib/liblzfse.a"
    install -Dm644 "${srcdir}/${_srcname}/LICENSE" "${pkgdir}/usr/share/licenses/lzfse/LICENSE"
}

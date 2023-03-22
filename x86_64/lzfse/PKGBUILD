# Maintainer: Laurent Tréguier <laurent@treguier.org>

pkgname=lzfse
pkgver=1.0
pkgrel=2
pkgdesc="The LZFSE compression library and command line tool"
arch=("i686" "x86_64")
url="https://github.com/lzfse/lzfse"
license=("BSD")
depends=()
makedepends=()
optdepends=()
provides=("lzfse")
conficts=("lzfse-git")
source=("https://github.com/lzfse/lzfse/archive/lzfse-${pkgver}.tar.gz") 
md5sums=('53e89f88d9cb0f4cb9c3f366dfb239a9')

build() {
    cd ${srcdir}/${pkgname}-${pkgname}-${pkgver}
    make
}

package() {
    install -Dm755 ${srcdir}/${pkgname}-${pkgname}-${pkgver}/build/bin/lzfse ${pkgdir}/usr/bin/lzfse
    install -d ${pkgdir}/usr/{include,lib}
    install -Dm644 ${srcdir}/${pkgname}-${pkgname}-${pkgver}/src/lzfse.h ${pkgdir}/usr/include/lzfse.h
    install -Dm644 ${srcdir}/${pkgname}-${pkgname}-${pkgver}/build/bin/liblzfse.a ${pkgdir}/usr/lib/
    install -d ${pkgdir}/usr/share/licenses/lzfse
    install -Dm644 ${srcdir}/${pkgname}-${pkgname}-${pkgver}/LICENSE ${pkgdir}/usr/share/licenses/lzfse/
}

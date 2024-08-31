# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=celt
pkgver=0.11.3
pkgrel=7
pkgdesc='Low-latency audio communication codec'
arch=('x86_64')
url='https://gitlab.xiph.org/xiph/celt/'
license=('BSD-2-Clause')
depends=('libogg')
source=("https://gitlab.xiph.org/xiph/celt/-/archive/v${pkgver}/celt-v${pkgver}.tar.bz2"
        '010-celt-fix-tandem-test.patch')
sha256sums=('e11a3ff390a733a470ca3ceb1f74c19770ee7c6f0ee169fdebc7b6efdc8700be'
            '233418e1cff4673e374a67ef7ee201a27f40ae38412a006ccd2d21882f512992')

prepare() {
    patch -d "${pkgname}-v${pkgver}" -Np1 -i "${srcdir}/010-celt-fix-tandem-test.patch"
    "${pkgname}-v${pkgver}/autogen.sh"
}

build() {
    # fix for tandem-test
    export CFLAGS="${CFLAGS/-Wp,-D_FORTIFY_SOURCE=?/}"
    
    cd "${pkgname}-v${pkgver}"
    ./configure --prefix='/usr' --enable-custom-modes
    make
}

check() {
    # fix for tandem-test
    export CFLAGS="${CFLAGS/-Wp,-D_FORTIFY_SOURCE=?/}"
    
    make -C "${pkgname}-v${pkgver}" check
}

package() {
    make -C "${pkgname}-v${pkgver}" DESTDIR="$pkgdir" install
    install -D -m644 "${pkgname}-v${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

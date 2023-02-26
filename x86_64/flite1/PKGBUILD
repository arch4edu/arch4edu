# Maintainer : Daniel Bermond <dbermond@archlinux.org>
# Contributor: der_FeniX <derfenix@gmail.com>
# Contributor: Albert Graef <aggraef@gmail.com>

pkgname=flite1
pkgver=1.4
pkgrel=5
pkgdesc='A lighweight speech synthesis engine (version 1.x)'
arch=('x86_64')
url='http://www.speech.cs.cmu.edu/flite/'
license=('custom')
depends=('glibc')
makedepends=('texlive-core' 'ed')
provides=("flite=${pkgver}" 'flite1-patched')
conflicts=('flite' 'flite1-patched')
replaces=('flite1-patched')
source=("http://www.festvox.org/flite/packed/flite-${pkgver}/flite-${pkgver}-release.tar.bz2"
        '010-flite1-tempfile-CVE-2014-0027.patch'
        '020-flite1-fix-parallel-builds.patch'
        '030-flite1-respect-destdir.patch'
        '040-flite1-ldflags.patch'
        '050-flite1-audio-interface.patch'
        '060-flite1-texi.patch'
        '070-flite1-texi2html-to-texi2any-migration.patch'
        '080-flite1-no-rpath.patch'
        '090-flite1-rename-conflicting-variable.patch')
sha256sums=('45c662160aeca6560589f78daf42ab62c6111dd4d244afc28118c4e6f553cd0c'
            '597f1516060917faab008819e3ceb5bb487f5b3948e97eef1020dc10b62c6edf'
            'bfd51888ea533bb9ee74cadb68b2e507cb715ab5043aa679b7f42ab52336a7a1'
            '093538c3a7cd2b9b9edd1f0956a34c4261c3ccdd4feb55e8ecedc338562495f3'
            'ff43e11241c9aea26483865c672c20421d12c688ae8b59b39471bafb52c1463e'
            '405320984e098c3d788b7751935b2774972ee7970dbe0fef0718ce1e5cc725c9'
            'd38fa5dfd4fef71970d904622ec106b9ac18ece002c671b14bc1ce9b342b56b6'
            '1b51d528e3927b80159c6f6c2155fc022f807db7a0cf19c50e9a5e5831086efb'
            '462b9ecdb3e4992cb2fc026b6483ec83d883ece530a3fa0794a00e4f6fbfbb1a'
            '9ad072d57d7b3d6a623f4885cf90a6548d6c5091cd00a7c0c8ff317f4fc0f7f1')

prepare() {
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/010-flite1-tempfile-CVE-2014-0027.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/020-flite1-fix-parallel-builds.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/030-flite1-respect-destdir.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/040-flite1-ldflags.patch"
    patch -d "flite-${pkgver}-release" -N   -i "${srcdir}/050-flite1-audio-interface.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/060-flite1-texi.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/070-flite1-texi2html-to-texi2any-migration.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/080-flite1-no-rpath.patch"
    patch -d "flite-${pkgver}-release" -Np1 -i "${srcdir}/090-flite1-rename-conflicting-variable.patch"
}

build() {
    cd "flite-${pkgver}-release"
    ./configure \
        --prefix='/usr' \
        --enable-shared \
        --disable-static \
        --with-vox='cmu_us_kal16'
    make -j1
    make -C doc flite.pdf
}

package() {
    make -C "flite-${pkgver}-release" DESTDIR="$pkgdir" install
    install -D -m644 "flite-${pkgver}-release/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 "flite-${pkgver}-release/doc/flite.pdf" -t "${pkgdir}/usr/share/doc/${pkgname}"
}

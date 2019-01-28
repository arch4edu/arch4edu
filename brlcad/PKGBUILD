pkgname=brlcad
pkgver=7.28.0
pkgrel=0
pkgdesc='An extensive 3D solid modeling system.'
url='https://brlcad.org'
license=('LGPL' 'BSD' 'custom:BDL')
arch=('i686' 'x86_64')
depends=('libgl' 'libxft' 'libxi')
makedepends=('cmake')
install="${pkgname}.install"
source=('build.patch' "http://downloads.sourceforge.net/sourceforge/${pkgname}/${pkgname}-${pkgver}.tar.bz2")
sha256sums=('SKIP' 'c6df320117fd50ecada5745a6f4c079b361df240915ed9c536aa1b697548a466')


prepare() {
    patch --quiet --strip=0 "--directory=${srcdir}/${pkgname}-${pkgver}" "--input=${srcdir}/build.patch"
}


build() {
    local _pkgprefix="/opt/${pkgname}"

    mkdir "${srcdir}/build"
    cd "${srcdir}/build"
    cmake -Wno-dev "${srcdir}/${pkgname}-${pkgver}" "-DCMAKE_INSTALL_PREFIX=${_pkgprefix}" \
        -DBRLCAD_ENABLE_COMPILER_WARNINGS=OFF -DBRLCAD_ENABLE_STRICT=OFF \
        -DCMAKE_BUILD_TYPE=Release -DBRLCAD_FLAGS_DEBUG=OFF -DBRLCAD_BUILD_STATIC_LIBS=OFF \
        -DBRLCAD_ENABLE_OPENGL=ON -DBRLCAD_BUNDLED_LIBS=BUNDLED -DBRLCAD_FREETYPE=OFF \
        -DBRLCAD_PNG=OFF -DBRLCAD_REGEX=OFF -DBRLCAD_ZLIB=OFF -DBRLCAD_ENABLE_QT=OFF
    make
    echo "export PATH=\"\$PATH:${_pkgprefix}/bin\"" >"${pkgname}.sh"
}


package() {
    cd "${srcdir}/build"
    make "DESTDIR=${pkgdir}" install
    install -D --mode=u=rw,go=r "--target-directory=${pkgdir}/usr/share/licenses/${pkgname}" share/doc/legal/{bdl,bsd}.txt
    install -D --mode=u=rw,go=r "--target-directory=${pkgdir}/etc/profile.d" "${pkgname}.sh"
}

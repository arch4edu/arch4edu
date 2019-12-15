pkgname=brlcad
pkgver=7.30.4
pkgrel=0
pkgdesc='An extensive 3D solid modeling system.'
url='https://brlcad.org'
license=('LGPL' 'BSD' 'custom:BDL')
arch=('i686' 'x86_64')
depends=('libgl' 'libxft' 'libxi')
makedepends=('cmake' 'subversion')
install="${pkgname}.install"
source=('build.patch' "${pkgname}-${pkgver}::svn+svn://svn.code.sf.net/p/${pkgname}/code/${pkgname}/tags/rel-${pkgver//./-}#revision=r74438")
sha256sums=('SKIP' 'SKIP')


_pkgprefix="/opt/${pkgname}"


prepare() {
    patch --quiet --strip=0 "--directory=${srcdir}/${pkgname}-${pkgver}" \
        "--input=${srcdir}/build.patch"
}


build() {
    cmake \
        -S "${srcdir}/${pkgname}-${pkgver}" \
        -B "${srcdir}/build" \
        -Wno-dev \
        "-DCMAKE_INSTALL_PREFIX=${_pkgprefix}" \
        -DBRLCAD_ENABLE_COMPILER_WARNINGS=OFF \
        -DBRLCAD_ENABLE_STRICT=OFF \
        -DCMAKE_BUILD_TYPE=Release \
        -DBRLCAD_FLAGS_DEBUG=OFF \
        -DBRLCAD_BUILD_STATIC_LIBS=OFF \
        -DBRLCAD_ENABLE_OPENGL=ON \
        -DBRLCAD_BUNDLED_LIBS=BUNDLED \
        -DBRLCAD_FREETYPE=OFF \
        -DBRLCAD_PNG=OFF \
        -DBRLCAD_REGEX=OFF \
        -DBRLCAD_ZLIB=OFF \
        -DBRLCAD_ENABLE_QT=OFF

    cmake --build "${srcdir}/build"

    echo "export PATH=\"\$PATH:${_pkgprefix}/bin\"" \
        >"${srcdir}/build/${pkgname}.sh"
}


package() {
    cmake --install "${srcdir}/build" --prefix "${pkgdir}${_pkgprefix}"

    install -D --mode=u=rw,go=r \
        "--target-directory=${pkgdir}/usr/share/licenses/${pkgname}" \
        "${srcdir}/build/share/doc/legal/"{bdl,bsd}.txt

    install -D --mode=u=rw,go=r \
        "--target-directory=${pkgdir}/etc/profile.d" \
        "${srcdir}/build/${pkgname}.sh"
}

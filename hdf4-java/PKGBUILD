# Maintainer : George Eleftheriou <eleftg>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4-java
_pkgname=hdf4
pkgver=4.2.14
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data (full version including the Java Native Interfaces - JNI)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support/HDF+4.2.14"
license=('custom')
depends=('zlib' 'libjpeg-turbo' 'libtirpc')
makedepends=('java-environment' 'gcc-fortran')
conflicts=('hdf4')
provides=('hdf4')
source=("https://support.hdfgroup.org/ftp/HDF/releases/HDF${pkgver}/src/hdf-${pkgver}.tar.bz2"
        "config.patch")
md5sums=('3f3bd5da84015e9221d26fb5a80094b4'
         'e17d14ac1d27012c1ea9ac03f783d355')

prepare() {
    cd "${srcdir}/hdf-${pkgver}"
    patch < "${srcdir}/config.patch"
    autoreconf -i
}

build() {
    cd "${srcdir}/hdf-${pkgver}"

    ./configure \
        CFLAGS="${CFLAGS} -fPIC" \
        LDFLAGS="-l:libjpeg.so.8 ${LDFLAGS}" \
        F77=gfortran \
        JAVADOC='javadoc -Xdoclint:none' \
        --enable-fortran \
        --enable-production \
        --enable-java \
        --with-zlib \
        --prefix=/opt/hdf4

    make
}

package() {
    cd "${srcdir}/hdf-${pkgver}"
    make -j1 DESTDIR="${pkgdir}" install
    mkdir -p "${pkgdir}/usr/share/licenses/${_pkgname}"
    cp "${srcdir}/hdf-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${_pkgname}"
}

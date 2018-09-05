# Maintainer : George Eleftheriou <eleftg>
# Contributor: Jingbei Li <petronny>
# Contributor: XavierCLL <xavier dot corredor dot llano at gmail dot com>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4
pkgver=4.2.14
pkgrel=2
pkgdesc="General purpose library and file format for storing scientific data (full version including the FORTRAN and the Java Native Interfaces - JNI)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support/HDF+4.2.14"
license=('custom')
depends=('libaec' 'zlib' 'libjpeg-turbo' 'libtirpc')
makedepends=('java-environment' 'gcc-fortran')
conflicts=('hdf4-java')
provides=('hdf4-java')
replaces=('hdf4-java')
source=("https://support.hdfgroup.org/ftp/HDF/releases/HDF${pkgver}/src/hdf-${pkgver}.tar.bz2"
        "config.patch")
md5sums=('3f3bd5da84015e9221d26fb5a80094b4'
         'e17d14ac1d27012c1ea9ac03f783d355')

prepare() {
    [ ! -d build ] && mkdir -p build
    cd "hdf-${pkgver}"
    patch < "${srcdir}/config.patch"
    autoreconf -i
}

build() {
    cd build

    "${srcdir}/hdf-${pkgver}"/configure \
        CFLAGS="${CFLAGS} -fPIC" \
        LIBS="-ljpeg -laec -lsz" \
        F77=gfortran \
        JAVADOC='javadoc -Xdoclint:none' \
        --enable-fortran \
        --enable-java \
        --enable-production \
        --with-zlib \
        --with-szlib=/usr \
        --prefix=/opt/hdf4

  make
}

package() {
    cd build
    make -j1 DESTDIR="${pkgdir}" install
    mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
    cp "${srcdir}/hdf-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}"
}

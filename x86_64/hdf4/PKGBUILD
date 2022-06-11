# Maintainer : George Eleftheriou <eleftg>
# Maintainer : XavierCLL <xavier dot corredor dot llano at gmail dot com>
# Contributor: Jingbei Li <petronny>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4
pkgver=4.2.15
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data (version including the Java Native Interfaces - JNI)"
arch=('x86_64')
url="https://portal.hdfgroup.org/display/support/HDF+4.2.15"
license=('custom')
depends=('libaec' 'zlib' 'libjpeg-turbo' 'libtirpc')
makedepends=('java-environment')
conflicts=('hdf4-java')
provides=('hdf4-java')
replaces=('hdf4-java')
source=("https://support.hdfgroup.org/ftp/HDF/releases/HDF${pkgver}/src/hdf-${pkgver}.tar.bz2")
md5sums=('27ab87b22c31906883a0bfaebced97cb')

prepare() {
    mkdir -p build
    cd "hdf-${pkgver}"
    autoreconf -i
}

build() {
    cd build

    "../hdf-${pkgver}"/configure \
        CFLAGS="${CFLAGS} -fPIC" \
        CPPFLAGS="${CPPFLAGS} -I/usr/include/tirpc/" \
        LDFLAGS="${LDFLAGS} -ltirpc" \
        FFLAGS="${FFLAGS} -fPIC -ffixed-line-length-none" \
        LIBS="${LIBS} -ljpeg -laec -lsz" \
        JAVADOC='javadoc -Xdoclint:none' \
        --enable-shared \
        --disable-static \
        --disable-fortran \
        --disable-netcdf \
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
    install -dm 755 "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm 644 "../hdf-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}"
    install -dm 755 "${pkgdir}/etc/ld.so.conf.d"
    echo "/opt/${pkgname}/lib" > "${pkgdir}"/etc/ld.so.conf.d/${pkgname}.conf
}


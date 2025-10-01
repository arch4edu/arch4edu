# Maintainer: XavierCLL
# Contributor: George Eleftheriou <eleftg>
# Contributor: Jingbei Li <petronny>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4
pkgver=4.3.1
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data"
arch=('x86_64')
url="https://portal.hdfgroup.org"
license=('custom')
depends=('libaec' 'zlib' 'libjpeg-turbo' 'libtirpc' 'netcdf')
makedepends=('autoconf' 'automake')
source=("https://github.com/HDFGroup/hdf4/archive/refs/tags/hdf${pkgver}.tar.gz")
sha256sums=('6dc3b8af610526788bf78fb3982b25a80abfc94e37ce0c3ae2929b5e9c937093')

prepare() {
    cd "${pkgname}-hdf${pkgver}"
    autoreconf -i
}

build() {
    cd "${pkgname}-hdf${pkgver}"

    ./configure \
        CFLAGS="${CFLAGS} -fPIC" \
        CPPFLAGS="${CPPFLAGS} -I/usr/include/tirpc/" \
        LDFLAGS="${LDFLAGS} -ltirpc" \
        FFLAGS="${FFLAGS} -fPIC -ffixed-line-length-none" \
        LIBS="${LIBS} -ljpeg -laec -lsz" \
        --enable-shared \
        --disable-static \
        --disable-fortran \
        --with-zlib \
        --with-szlib=yes \
        --prefix=/opt/hdf4
    make
}

package() {
    cd "${pkgname}-hdf${pkgver}"
    make -j1 DESTDIR="${pkgdir}" install
    install -dm 755 "${pkgdir}/usr/share/licenses/${pkgname}"
    install -Dm 644 "COPYING" "${pkgdir}/usr/share/licenses/${pkgname}"
    install -dm 755 "${pkgdir}/etc/ld.so.conf.d/"
    echo "/opt/${pkgname}/lib" > "${pkgdir}/etc/ld.so.conf.d/${pkgname}.conf"
}


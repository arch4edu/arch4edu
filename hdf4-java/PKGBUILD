# Maintainer : George Eleftheriou <eleftg>
# Contributor: David Scholl <djscholl at gmail dot com>

pkgname=hdf4-java
_pkgname=hdf4
pkgver=2.13
pkgrel=4
pkgdesc="General purpose library and file format for storing scientific data (full version including the Java Native Interfaces - JNI)"
arch=('i686' 'x86_64')
url="http://www.hdfgroup.org/hdf4.html"
license=('custom')
depends=('zlib' 'libjpeg-turbo' 'libtirpc')
makedepends=('java-environment' 'gcc-fortran')
conflicts=('hdf4')
provides=('hdf4')
source=("http://www.hdfgroup.org/ftp/HDF/HDF_Current/src/hdf-4.2.13.tar.bz2"
        "config.patch")
md5sums=('2c1b6c7fdf97738251154680b37bd86a'
         'e16254cdd55c1a2653b31ec1bdc4b711')

prepare() {
  cd "${srcdir}/hdf-4.2.13"
  patch < "${srcdir}/config.patch"
  autoreconf -i
}

build() {
  cd "${srcdir}/hdf-4.2.13"

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
  cd "${srcdir}/hdf-4.2.13"
  make -j1 DESTDIR="${pkgdir}" install
  mkdir -p "${pkgdir}/usr/share/licenses/${_pkgname}"
  cp "${srcdir}/hdf-4.2.13/COPYING" "${pkgdir}/usr/share/licenses/${_pkgname}"
}

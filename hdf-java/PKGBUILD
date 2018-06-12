# Maintainer: George Eleftheriou

pkgname=hdf-java
_pkgname=${pkgname/-/}
pkgver=3.3.2
pkgrel=4
pkgdesc="The hdf5 Java Native Interfaces (JNI) for 32-bit object ids (files created with versions up to 1.8)"
arch=('x86_64')
url="https://support.hdfgroup.org/products/java/"
license=('custom')
makedepends=('java-environment' 'cmake' 'apache-ant')
depends=()
source=("http://www.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/hdfjni-${pkgver}/src/CMake-${_pkgname}-${pkgver}.tar.gz"
       FindXDR.patch)
md5sums=('9fdbb55f2292092f0e6b46078109d54a'
         '97b03ee821863fd80b4c50aa75c9d791')

prepare() {
  cd "CMake-${_pkgname}-${pkgver}"

  # change install prefix
  sed -i "s;DCMAKE_INSTALL_PREFIX:PATH=\${INSTALLDIR};DCMAKE_INSTALL_PREFIX:PATH=/opt/${_pkgname}-${pkgver};" HDFJavaconfig.cmake

  # fix reported issues about finding JNI (?)
  rm "${_pkgname}-${pkgver}/config/cmake/FindJNI.cmake"

  # fix FindXDR issue
  tar -xf HDF4.tar.gz
  rm HDF4.tar.gz
  patch -p1 < "${srcdir}/FindXDR.patch"
  tar -cf - hdf-4.2.13 | gzip -9 > HDF4.tar.gz
  rm -r hdf-4.2.13
}

build() {
  cd "CMake-${_pkgname}-${pkgver}"
  ./build-hdfjava-unix.sh
}

package() {
  cd "CMake-${_pkgname}-${pkgver}/build"
  make -j1 DESTDIR=${pkgdir} install
}

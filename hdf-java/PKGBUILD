# Maintainer: George Eleftheriou

pkgname=hdf-java
_pkgname=${pkgname/-/}
pkgver=3.3.2
pkgrel=3
pkgdesc="The hdf5 Java Native Interfaces (JNI) for 32-bit object ids (files created with versions up to 1.8)"
arch=('i686' 'x86_64')
url="https://support.hdfgroup.org/products/java/"
license=('custom')
makedepends=('java-environment' 'cmake' 'apache-ant')
depends=()
source=("http://www.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/hdfjni-${pkgver}/src/CMake-${pkgname/-/}-${pkgver}.tar.gz")
md5sums=('9fdbb55f2292092f0e6b46078109d54a')

prepare() {
  cd "CMake-${pkgname/-/}-${pkgver}"
  sed -i "s;DCMAKE_INSTALL_PREFIX:PATH=\${INSTALLDIR};DCMAKE_INSTALL_PREFIX:PATH=/opt/${pkgname/-/}-${pkgver};" HDFJavaconfig.cmake
  # fix reported issues about finding JNI (?)
  rm "${_pkgname}-${pkgver}/config/cmake/FindJNI.cmake"
}

build() {
  cd "CMake-${pkgname/-/}-${pkgver}"
  ./build-hdfjava-unix.sh
}

package() {
  cd "CMake-${pkgname/-/}-${pkgver}/build"
  make -j1 DESTDIR=${pkgdir} install
}

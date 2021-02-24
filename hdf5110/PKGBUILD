# $Id$
# Maintainer: Grey Christoforo <first name at last name dot net>

pkgname=hdf5110
pkgver=1.10.7
_pkgver=${pkgver%.*}
pkgrel=1
pkgdesc="General purpose library and file format for storing scientific data, legacy 1.10 branch w/java bindings"
arch=(x86_64)
url="https://www.hdfgroup.org/hdf5"
license=(custom)
depends=(
zlib
libaec
bash
)
makedepends=(
cmake
time
inetutils
gcc-fortran
jdk-openjdk
)
options=('staticlibs')
source=("${pkgname}-${pkgver}.tar.gz::https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-${_pkgver}/hdf5-${pkgver}/src/CMake-hdf5-${pkgver}.tar.gz")
sha256sums=('651bb79a4b19b60ab9f99092f7c4cf61b7c6ca2c9bd545717746a5a47839a5bb')

# as per
# https://portal.hdfgroup.org/display/support/Building+HDF5+with+CMake
# and
# https://portal.hdfgroup.org/display/support/How+to+Change+HDF5+CMake+Build+Options

prepare(){
  cd CMake-hdf5-${pkgver}

  # enable java
  sed '/^set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_BUILD_JAVA:BOOL=OFF")/s/^/#/g' -i HDF5options.cmake
  sed '/^#set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_BUILD_JAVA:BOOL=ON")/s/^#//g' -i HDF5options.cmake

  # enable fortran
  sed '/^set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_BUILD_FORTRAN:BOOL=OFF")/s/^/#/g' -i HDF5options.cmake
  sed '/^#set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_BUILD_FORTRAN:BOOL=ON")/s/^#//g' -i HDF5options.cmake

  # I don't know why I wouldn't want thread safety...but this doesn't build. missing pthread dep?
  #sed '/^#set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_THREADSAFE:BOOL=ON")/s/^#//g' -i HDF5options.cmake 

  # don't package external libs
  sed '/^set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_PACKAGE_EXTLIBS:BOOL=ON")/s/^/#/g' -i HDF5options.cmake

  # enable zlib and szlib
  sed '/HDF5_ENABLE_Z_LIB_SUPPORT/c\set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_Z_LIB_SUPPORT:BOOL=ON")' -i HDF5options.cmake
  sed '/HDF5_ENABLE_SZIP_SUPPORT/c\set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_SZIP_SUPPORT:BOOL=ON")' -i HDF5options.cmake
  sed '/HDF5_ENABLE_SZIP_ENCODING/c\set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ENABLE_SZIP_ENCODING:BOOL=ON")' -i HDF5options.cmake

  # zlib and szlib are not "external"
  sed '/^set (ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DHDF5_ALLOW_EXTERNAL_SUPPORT:STRING=TGZ -DTGZPATH:PATH=${CTEST_SCRIPT_DIRECTORY}")/s/^/#/g' -i HDF5options.cmake
}

build(){
  cd CMake-hdf5-${pkgver}
  ctest -S HDF5config.cmake,BUILD_GENERATOR=Unix,INSTALLDIR=/opt/${pkgname} -C Release -V -O hdf5.log
  #./build-unix.sh
  cd build
  make
}

package() {
  cd "${srcdir}/CMake-hdf5-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  install -Dm644 ../hdf5-${pkgver}/COPYING -t "${pkgdir}"/opt/${pkgname}/share/licenses/${pkgname}

  # Fix 1.6 compatibility for h5py, is this still needed?
  #cd "${pkgdir}"/usr/include/
  #patch -p1 -i "${srcdir}"/hdf5-1.12.0-compat-1.6.patch
}


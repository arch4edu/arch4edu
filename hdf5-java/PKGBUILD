# $Id$
# Maintainer: Grey Christoforo <first name at last name dot net>

pkgname=hdf5-java
pkgver=1.12.0
_pkgver=${pkgver%.*}
pkgrel=3
pkgdesc="General purpose library and file format for storing scientific data , w/java bindings"
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
gcc-fortran
jdk-openjdk
inetutils
)
replaces=(hdf5-cpp-fortran)
provides=(hdf5-cpp-fortran hdf5)
conflicts=(hdf5)
options=('staticlibs')
source=("${pkgname}-${pkgver}.tar.gz::https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-${_pkgver}/hdf5-${pkgver}/src/CMake-hdf5-${pkgver}.tar.gz"
	"hdf5-1.12.0-compat-1.6.patch")
sha256sums=('01b9c01c45cc8c66da86e69c510e17f3cff0706a65d8683cd86af405eaf75397'
            '72ad497c56760bb3af8193c88d3fa264125829850b843697de55d934c56f7f44')

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

  # use legacy API
  #echo 'set(ADD_BUILD_OPTIONS "${ADD_BUILD_OPTIONS} -DDEFAULT_API_VERSION:STRING=v110")' >> HDF5options.cmake

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
  ctest -S HDF5config.cmake,BUILD_GENERATOR=Unix,INSTALLDIR=/usr -C Release -V -O hdf5.log
  #./build-unix.sh
  cd build
  make
}

package() {
  cd "${srcdir}/CMake-hdf5-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  install -Dm644 ../hdf5-${pkgver}/COPYING -t "${pkgdir}"/usr/share/licenses/${pkgname}

  # Fix 1.6 compatibility for h5py, is this still needed?
  #cd "${pkgdir}"/usr/include/
  #patch -p1 -i "${srcdir}"/hdf5-1.12.0-compat-1.6.patch
}


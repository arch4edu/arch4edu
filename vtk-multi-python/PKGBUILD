# $Id$
# Maintainer: Ray Rashif <schiv@archlinux.org>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Oliver Mader <b52@reaktor42.de>

pkgbase='vtk-multi-python'
pkgname=('vtk-base' 'python2-vtk' 'python-vtk')
pkgver=7.1.1
_majorver=7.1
pkgrel=1
arch=('i686' 'x86_64')
url='http://www.vtk.org/'
license=('BSD')
depends=('gcc-libs')
conflicts=('vtk' 'vtk6')
makedepends=('boost' 'cmake' 'ninja' 'java-environment' 'doxygen' 'gnuplot' 'tk' 'wget' 'python2-matplotlib' 'python2-twisted' 'python2-mpi4py' 'python2-autobahn' 'python-matplotlib' 'python-twisted' 'python-mpi4py' 'python-autobahn' 'unixodbc' 'gdal' 'openmpi' 'mariadb' 'glew' 'ffmpeg' 'lesstif' 'qt5-base' 'qt5-x11extras' 'qt5-tools' 'qt5-webkit' 'jsoncpp')
optdepends=('java-runtime: java bindings'
            'tk: tcl bindings'
            'gnuplot: plotting tools'
	    'python-vtk: Python 3 API'
	    'python2-vtk: Python 2 API'
            'graphviz: drawing tools'
            'openmpi: OpenMPI support'
            'qt5-x11extras'
            'qt5-webkit: WebKit support'
            'unixodbc'
            'glew'
            'gdal'
            'mariadb'
            'ffmpeg'
            'jsoncpp')
source=("http://www.vtk.org/files/release/${_majorver}/VTK-${pkgver}.tar.gz"
        "http://www.vtk.org/files/release/${_majorver}/VTKData-${pkgver}.tar.gz"
        "http://www.vtk.org/files/release/${_majorver}/VTKLargeData-${pkgver}.tar.gz"
	'soversion-sharedlibs.patch'
	'python-suffix.patch')
options=(staticlibs !emptydirs)
sha1sums=('8b3433e408ba3408354356dee4d295ea599a817c'
          'e0021056162e72e0dac20fa833ea4f9ee29dee48'
          '1ba20c351ac8237c168198a89504c3d93ea699c7'
          '823f10356ddc86d22629ee5a804f22145af91b6d'
          'a597aa42e6f623b346c16db36aea31df29bdd8da')

prepare() {
  cd "${srcdir}/VTK-${pkgver}"

  patch -p1 -i "${srcdir}/soversion-sharedlibs.patch"
  patch -p1 -i "${srcdir}/python-suffix.patch"
}

build() {
  cd "${srcdir}"

  rm -rf build-py2 build-py3
  mkdir build-py2 build-py3

  # to help cmake find java
  export JAVA_HOME=/usr/lib/jvm/default

  # flags to enable using system libs
  local cmake_system_flags=""
  # TODO: try to use system provided XDMF2, XDMF3, LIBPROJ4 NETCDF, HDF5
  # VTK fails to compile with recent netcdf-cxx package, VTK should be ported to the latest API
  # VTK does not work with XDMF2 compiled from git. TODO: make vtk compatible with system XDMF library.
  # Note: VTK explicitly disables system GLEW dependency, it uses embedded sources with modifications
  # Note: system HDF5 is incompatible
  for lib in EXPAT FREETYPE JPEG PNG TIFF ZLIB LIBXML2 OGGTHEORA TWISTED ZOPE SIX AUTOBAHN MPI4PY JSONCPP GLEW; do
    cmake_system_flags+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
  done

  cd build-py2

  local _tkver=$(echo 'puts $tcl_version' | tclsh)

  # flags to use python2 instead of python which is 3.x.x on archlinux
  # system gl2ps is not used because of http://www.vtk.org/Bug/view.php?id=16083
  local cmake_system_python_flags="-DPYTHON_EXECUTABLE:PATH=/usr/bin/python2 -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python2.7 -DPYTHON_LIBRARY:PATH=/usr/lib/libpython2.7.so"

  cmake \
    -Wno-dev \
    -DVTK_USE_SYSTEM_HDF5:BOOL=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:FILEPATH=/usr \
    -DBUILD_DOCUMENTATION:BOOL=ON \
    -DDOCUMENTATION_HTML_HELP:BOOL=ON \
    -DDOCUMENTATION_HTML_TARZ:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DVTK_USE_FFMPEG_ENCODER:BOOL=ON \
    -DVTK_BUILD_ALL_MODULES:BOOL=ON \
    -DVTK_USE_LARGE_DATA:BOOL=ON \
    -DVTK_QT_VERSION:STRING="5" \
    -DVTK_WRAP_JAVA:BOOL=ON \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DVTK_WRAP_TCL:BOOL=ON \
    -DCMAKE_CXX_FLAGS="-D__STDC_CONSTANT_MACROS" \
    -DVTK_CUSTOM_LIBRARY_SUFFIX="" \
    -DVTK_INSTALL_INCLUDE_DIR:PATH=include/vtk \
    -DVTK_INSTALL_TCL_DIR=/usr/lib/tcl${_tkver}/vtk/ \
    ${cmake_system_flags} \
    ${cmake_system_python_flags} \
    -DCMAKE_BUILD_TYPE=Release \
    "${srcdir}/VTK-$pkgver" \
    -GNinja

  ninja

  cd ../build-py3

  local cmake_system_python_flags="-DPYTHON_EXECUTABLE:PATH=/usr/bin/python -DPYTHON_INCLUDE_DIR:PATH=/usr/include/python3.6m -DPYTHON_LIBRARY:PATH=/usr/lib/libpython3.6m.so"

  cmake \
    -Wno-dev \
    -DVTK_USE_SYSTEM_HDF5:BOOL=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:FILEPATH=/usr \
    -DBUILD_DOCUMENTATION:BOOL=ON \
    -DDOCUMENTATION_HTML_HELP:BOOL=ON \
    -DDOCUMENTATION_HTML_TARZ:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DVTK_USE_FFMPEG_ENCODER:BOOL=ON \
    -DVTK_BUILD_ALL_MODULES:BOOL=ON \
    -DVTK_USE_LARGE_DATA:BOOL=ON \
    -DVTK_QT_VERSION:STRING="5" \
    -DVTK_WRAP_JAVA:BOOL=ON \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DVTK_WRAP_TCL:BOOL=ON \
    -DCMAKE_CXX_FLAGS="-D__STDC_CONSTANT_MACROS" \
    -DVTK_CUSTOM_LIBRARY_SUFFIX="" \
    -DVTK_INSTALL_INCLUDE_DIR:PATH=include/vtk \
    -DVTK_INSTALL_TCL_DIR=/usr/lib/tcl${_tkver}/vtk/ \
    ${cmake_system_flags} \
    ${cmake_system_python_flags} \
    -DCMAKE_BUILD_TYPE=Release \
    "${srcdir}/VTK-$pkgver" \
    -GNinja

  ninja
}

package_vtk-base() {
  pkgdesc='A software system for 3D computer graphics, image processing, and visualization'

  cd "${srcdir}/build-py3"

  DESTDIR="${pkgdir}" ninja install

  # Python stuff in seperate packages
  find "${pkgdir}" -ipath "${pkgdir}"'*python*' \( -type f -o -type l \) -delete

  # Move the vtk.jar to the arch-specific location
  install -dv "${pkgdir}/usr/share/java/vtk"
  mv -v "${pkgdir}/usr/lib/vtk.jar" "${pkgdir}/usr/share/java/vtk"
  rm -rf "${pkgdir}/usr/lib/vtk-${_majorver}/java"

  # Install license
  install -dv "${pkgdir}/usr/share/licenses/vtk"
  install -m644 "${srcdir}/VTK-$pkgver/Copyright.txt" "${pkgdir}/usr/share/licenses/vtk"

  # Fix path of QtDesigner plugin
  install -dv "${pkgdir}/usr/lib/qt5"
  mv "$pkgdir"/usr/plugins "$pkgdir"/usr/lib/qt5/plugins
}

package_python-vtk() {
  pkgdesc='Python bindings for VTK'
  depends=('vtk-base' 'python-matplotlib' 'python-twisted' 'python-autobahn' 'python-mpi4py' 'gdal' 'unixodbc')

  cd "${srcdir}/build-py3"

  DESTDIR="${pkgdir}" ninja install

  find "${pkgdir}" ! -ipath "${pkgdir}"'*python*' \( -type f -o -type l \) -delete
}

package_python2-vtk() {
  pkgdesc='Python bindings for VTK'
  depends=('vtk-base' 'python2-matplotlib' 'python2-twisted' 'python2-autobahn' 'python2-mpi4py')

  cd "${srcdir}/build-py2"

  DESTDIR="${pkgdir}" ninja install

  find "${pkgdir}" ! \( -path '*/usr/lib/python2.7/*' -o -name 'vtkpython' -o -name 'pvtkpython' -o -name '*Python27*' -o -name '*Py27*' \) \( -type f -o -type l \) -delete

  mv "${pkgdir}/usr/bin/vtkpython" "${pkgdir}/usr/bin/vtkpython2"
  mv "${pkgdir}/usr/bin/pvtkpython" "${pkgdir}/usr/bin/pvtkpython2"

  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find "${pkgdir}" -name '*.py')
}


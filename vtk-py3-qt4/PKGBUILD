# $Id$
# vtk package fork build with python3 and qt4 bindings
# Maintainer: Alex Maystrenko <alexeytech@gmail.com>

# upstream Arch Linux vtk package maintainers:
# Maintainer: Ray Rashif <schiv@archlinux.org>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >

pkgname=vtk-py3-qt4
pkgver=8.0.0
_majorver=8.0
pkgrel=5
pkgdesc='A software system for 3D computer graphics, image processing, and visualization, build with python3 and qt4 bindings'
arch=('i686' 'x86_64')
url='http://www.vtk.org/'
license=('BSD')
depends=('gcc-libs' 'gl2ps' 'qt4')
conflicts=('vtk' 'python-constantly' 'python-incremental')
makedepends=('boost' 'cmake' 'ninja' 'java-environment' 'doxygen' 'gnuplot' 'tk' 'wget' 'python-matplotlib' 'python-twisted' 'python-mpi4py' 'python-autobahn' 'unixodbc' 'gdal' 'openmpi' 'mariadb' 'glew' 'ffmpeg' 'lesstif' 'qtwebkit' 'qt5-webkit' 'jsoncpp')
optdepends=('python: python bindings'
            'java-runtime: java bindings'
            'tk: tcl bindings'
            'gnuplot: plotting tools'
            'graphviz: drawing tools'
            'python-matplotlib: for Matplotlib rendering'
            'python-twisted: for vtkWeb'
            'python-autobahn: for vtkWeb'
            'openmpi: OpenMPI support'
            'python-mpi4py: OpenMPI python support'
            'unixodbc'
            'glew'
            'gdal'
            'mariadb'
            'ffmpeg'
            'jsoncpp')
source=("http://www.vtk.org/files/release/${_majorver}/VTK-${pkgver}.tar.gz"
        "http://www.vtk.org/files/release/${_majorver}/VTKData-${pkgver}.tar.gz"
        "http://www.vtk.org/files/release/${_majorver}/VTKLargeData-${pkgver}.tar.gz"
        )
options=(staticlibs !strip)
sha1sums=('a1bc6a8335b02f01a23cb6e96c4613d12ab598ed'
          'e4d7315f27f42ce0820721b5d4304913fd4720c3'  
          '2167822c8ebda61e04c3fce71692621f2b24d06b' 
          )

prepare() {
  cd "${srcdir}"/VTK-$pkgver
}

build() {
  cd "${srcdir}"
  test -d build && msg2 "note: using existing build directory"
  mkdir -p build
  cd build
  # HACK: vtk does not install if this directory is not created
  mkdir -p Utilities/Doxygen/doc/html

  # to help cmake find java
  export JAVA_HOME=/usr/lib/jvm/default

  # flags to enable using system libs
  local cmake_system_flags=""
  # TODO: try to use system provided XDMF2, XDMF3, LIBPROJ4 NETCDF
  # VTK fails to compile with recent netcdf-cxx package, VTK should be ported to the latest API
  # VTK does not work with XDMF2 compiled from git. TODO: make vtk compatible with system XDMF library. 
  # Note: VTK explicitly disables system GLEW dependency, it uses embedded sources with modifications
  for lib in EXPAT FREETYPE JPEG PNG TIFF ZLIB LIBXML2 OGGTHEORA TWISTED ZOPE SIX AUTOBAHN MPI4PY JSONCPP GLEW; do
    cmake_system_flags+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
  done

  local _tkver=$(echo 'puts $tcl_version' | tclsh)

  # Compilation bug http://www.vtk.org/Bug/view.php?id=16083
  # requires -DVTK_USE_SYSTEM_GL2PS=OFF

  cmake \
    -Wno-dev \
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
    -DVTK_QT_VERSION:STRING="4" \
    -DVTK_WRAP_JAVA:BOOL=ON \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DVTK_PYTHON_VERSION="3" \
    -DVTK_WRAP_TCL:BOOL=ON \
    -DVTK_USE_SYSTEM_GL2PS=OFF \
    -DCMAKE_CXX_FLAGS="-D__STDC_CONSTANT_MACROS" \
    -DVTK_CUSTOM_LIBRARY_SUFFIX="" \
    -DVTK_INSTALL_INCLUDE_DIR:PATH=include/vtk \
    -DVTK_INSTALL_TCL_DIR=/usr/lib/tcl${_tkver}/vtk/ \
    -DBUILD_TESTING:BOOL=OFF \
    ${cmake_system_flags} \
    -DCMAKE_BUILD_TYPE=Release \
    "${srcdir}/VTK-$pkgver" \
    -GNinja

  ninja
}

check() {
  cd "${srcdir}/build"
  msg2 "testing disabled, see PKGBUILD"
  #ctest
}

package() {
  cd "${srcdir}/build"

  DESTDIR="${pkgdir}" ninja install

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


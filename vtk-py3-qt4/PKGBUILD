# $Id$
# vtk package fork build with python3 and qt4 bindings
# Maintainer: Alex Maystrenko <alexeytech@gmail.com>

# upstream Arch Linux vtk package maintainers:
# Maintainer: Ray Rashif <schiv@archlinux.org>
# Contributor: Andrzej Giniewicz <gginiu@gmail.com>
# Contributor: Thomas Dziedzic < gostrc at gmail >

pkgname=vtk-py3-qt4
pkgver=7.0.0
_majorver=7.0
pkgrel=3
pkgdesc='A software system for 3D computer graphics, image processing, and visualization, build with python3 and qt4 bindings'
arch=('i686' 'x86_64')
url='http://www.vtk.org/'
license=('BSD')
depends=('gcc-libs' 'gl2ps')
coflicts=('vtk')
makedepends=('boost' 'cmake' 'ninja' 'java-environment' 'doxygen' 'gnuplot' 'tk' 'wget' 'python-matplotlib' 'python-twisted' 'python-mpi4py' 'python-autobahn' 'unixodbc' 'gdal' 'openmpi' 'mariadb' 'glew' 'ffmpeg' 'lesstif' 'qt4' 'qtwebkit' 'jsoncpp')
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
        gdal2.patch
        ffmpeg3_compat.patch
        remove_args.patch
        find_gcc6.patch
        fix-possible-segfault.patch
        fix-qt4-moc.patch)
options=(staticlibs !strip)
sha1sums=('7719fac36b36965eaf5076542166ba49bbe7afbb'
          '1bbaa642a3e3676a58a08c956df73645326c2859'
          '8d16a1fba15e4eb95c03fe97937488ddcdd7fbd0'
          'c60610e7c8cf0ad93d7c02cbf8a20fc415f59b3e'
          'a78177f8dd6dedd9ad189fa12730ec53c7d02508'
          'd880f0f7d979cc9efa9246eda82880fef29172c2'
          '127d302f46e2691980af83350542243ab76ca75f'
          '1b04eadd40b823092d620914ce5bc8314e1e4980'
          '9b1523da7b111a02390e85a5eee2b015680d05ea')

prepare() {
  cd "${srcdir}"/VTK-$pkgver

  patch -p1 < ../ffmpeg3_compat.patch # http://www.vtk.org/Bug/view.php?id=16001
  patch -p1 < ../gdal2.patch # https://github.com/Kitware/VTK/pull/21
  patch -p1 < ../remove_args.patch # https://gitlab.kitware.com/vtk/vtk/commit/52501fd085a64b55d1b53d40c1d3f86c6ce9addd
  patch -p1 < ../find_gcc6.patch # https://gitlab.kitware.com/vtk/vtk/commit/06e2a00bf8accb04db63b3c1c7a454e4afc6fea6
  patch -p1 < ../fix-possible-segfault.patch
  patch -p1 < ../fix-qt4-moc.patch

}

build() {
  cd "${srcdir}"
  test -d build && msg2 "note: using existing build directory"
  mkdir -p build
  cd build

  # to help cmake find java
  export JAVA_HOME=/usr/lib/jvm/default

  # flags to enable using system libs
  local cmake_system_flags=""
  # TODO: try to use system provided XDMF2, XDMF3, LIBPROJ4 NETCDF
  # VTK fails to compile with recent netcdf-cxx package, VTK should be ported to the latest API
  # VTK does not work with XDMF2 compiled from git. TODO: make vtk compatible with system XDMF library. 
  # Note: VTK explicitly disables system GLEW dependency, it uses embedded sources with modifications
  for lib in EXPAT FREETYPE JPEG PNG TIFF ZLIB LIBXML2 OGGTHEORA TWISTED ZOPE SIX AUTOBAHN MPI4PY JSONCPP GLEW GL2PS; do
    cmake_system_flags+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
  done

  local _tkver=$(echo 'puts $tcl_version' | tclsh)

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


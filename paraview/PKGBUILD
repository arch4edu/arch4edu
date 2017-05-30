# Maintainer:  Oliver Goethel <deezy>
# Contributor: eolianoe eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Mathias Anselmann <mathias.anselmann@gmail.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Michele Mocciola <mickele>
# Contributor: Simon Zilliken <simon____AT____zilliken____DOT____name>
# Contributor: chuckdaniels

pkgname=paraview
_pkgver=5.3.0
pkgver=${_pkgver//-/.}
pkgrel=3
pkgdesc='Parallel Visualization Application using VTK'
arch=('i686' 'x86_64')
url='http://www.paraview.org'
license=('custom')
depends=('qt5-tools' 'qt5-x11extras'  'qt5-xmlpatterns'
         'openmpi' 'python-matplotlib' 'python-numpy' 'ffmpeg' 'boost' 'glew'
         'expat' 'freetype2' 'libjpeg' 'libxml2' 'libtheora' 'libpng' 'libtiff' 'zlib'
         'ospray' 'cgns')
makedepends=('cmake' 'mesa' 'gcc-fortran')
source=("http://paraview.org/files/v${pkgver:0:3}/ParaView-v${_pkgver}.tar.gz"
        'paraview-desktop.patch')
sha1sums=('c8a31039b189e63b20618bbfa91e89555ce62b6d'
          'd7da23daca34cd015294c4d2f702cdc4a81f0853')

prepare() {
  cd "${srcdir}/ParaView-v${_pkgver}"

  patch -p1 -i ../paraview-desktop.patch

  #rm -rf "${srcdir}/build"
  mkdir -p "${srcdir}/build"
}

build() {
  cd "${srcdir}/build"

  # flags to enable system libs
  # add PROTOBUF when https://gitlab.kitware.com/paraview/paraview/issues/13656 gets fixed
  local VTK_USE_SYSTEM_LIB=""
  for lib in EXPAT FREETYPE GLEW HDF5 JPEG LIBXML2 OGGTHEORA PNG TIFF ZLIB; do
    VTK_USE_SYSTEM_LIB+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
  done

  cmake \
    -DBUILD_DOCUMENTATION:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER=mpicc \
    -DCMAKE_CXX_COMPILER=mpicxx \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
    -DOSPRAY_INSTALL_DIR:PATH=/usr \
    -DPARAVIEW_ENABLE_CGNS:BOOL=ON \
    -DPARAVIEW_ENABLE_FFMPEG:BOOL=ON \
    -DPARAVIEW_ENABLE_MATPLOTLIB:BOOL=ON \
    -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
    -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
    -DPARAVIEW_QT_VERSION=5 \
    -DPARAVIEW_USE_MPI:BOOL=ON \
    -DPARAVIEW_USE_VISITBRIDGE:BOOL=ON \
    -DPARAVIEW_USE_OSPRAY:BOOL=ON \
    -DVISIT_BUILD_READER_CGNS:BOOL=ON \
    -DVTK_PYTHON_VERSION=3 \
    -DVTK_QT_VERSION=5 \
    -DVTK_RENDERING_BACKEND:STRING=OpenGL2 \
    -DVTK_SMP_IMPLEMENTATION_TYPE:STRING=OpenMP \
    ${VTK_USE_SYSTEM_LIB} \
    ../ParaView-v${_pkgver}

  make
}

package() {
  cd "${srcdir}/build"

  make DESTDIR="${pkgdir}" install

  #Install license
  install -Dm644 "${srcdir}/ParaView-v${_pkgver}/License_v1.2.txt" "${pkgdir}/usr/share/licenses/paraview/LICENSE"

  # Remove IceT man pages to avoid conflicts
  rm -- "${pkgdir}/usr/share/man/man3/icet"*.3
}

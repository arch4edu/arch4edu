# Maintainer : bartus <arch-user-repoᘓbartus.33mail.com>
# Contributor: Bruno Pagani <archange@archlinux.org>
# Contributor: Oliver Goethel <deezy>
# Contributor: eolianoe eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: George Eleftheriou <eleftg>
# Contributor: Mathias Anselmann <mathias.anselmann@gmail.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Michele Mocciola <mickele>
# Contributor: Simon Zilliken <simon____AT____zilliken____DOT____name>
# Contributor: chuckdaniels

_pkg=paraview
_mpi=openmpi
pkgname=${_pkg}-opt
#-${_mpi}
pkgver=5.6.0
pkgrel=5
provides=(${_pkg})
conflicts=(${_pkg})
pkgdesc="Parallel Visualization application using VTK (${_mpi} version): installed to /opt/"
arch=('x86_64')
url="https://www.paraview.org"
license=('BSD' 'custom')
depends=('boost-libs' 'qt5-tools' 'qt5-x11extras' 'intel-tbb' 'openmpi'
         'ffmpeg' 'ospray' 'python-matplotlib' 'python-numpy'
         'cgns' 'protobuf' 'python-pygments'
         'double-conversion' 'expat' 'freetype2' 'glew' 'hdf5' 
         'libjpeg' 'jsoncpp' 'libxml2' 'lz4' 'xz' 'python-mpi4py' 'netcdf'
         'libogg' 'libpng' 'pugixml' 'libtheora' 'libtiff' 'zlib')
#        gl2ps
#        netcdf-cxx libharu
#        proj, sqlite apparently not used in this VTK configuration
makedepends=('cmake' 'boost' 'mesa' 'gcc-fortran' 'ninja' 'qt5-tools' 'qt5-xmlpatterns' 'eigen' 'pegtl')
source=("${url}/files/v${pkgver:0:3}/ParaView-v${pkgver}.tar.xz"
	"paraview.sh")
sha256sums=('5b49cb96ab78eee0427e25200530ac892f9a3da7725109ce1790f8010cb5b377'
            'ed1d597139473f24441e5c10038e988d64ab1d904e0c5ecaf24069734989bff4')

prepare() {
    mkdir -p build
}

build() {
    cd build

    # Flags to enable system libs in VTK building, as in VTK package
    # GL2PS has non-upstreamed patches?
    # KISSFFT is not packaged
    # UTF8 (utfcpp) is not packaged (but present in AUR)
    # VERDICT is not packaged
    # ZFP is not packaged
    # NETCDFCPP blocked by https://github.com/Unidata/netcdf-cxx4/issues/43
    # LIBHARU blocked by https://github.com/libharu/libharu/pull/157
    # LIBPROJ4, SQLITE apparently not used in this VTK configuration
    local VTK_USE_SYSTEM_LIB=""
    for lib in DOUBLECONVERSION EIGEN EXPAT FREETYPE GLEW HDF5 JPEG JSONCPP LIBXML2 LZ4 LZMA MPI4PY NETCDF OGG PEGTL PNG PUGIXML THEORA TIFF ZLIB
    do
        VTK_USE_SYSTEM_LIB+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
    done
    # Specific system libs for ParaView version
    for lib in CGNS PROTOBUF PYGMENTS
    do
        VTK_USE_SYSTEM_LIB+="-DVTK_USE_SYSTEM_${lib}:BOOL=ON "
    done

    cmake ../ParaView-v${pkgver} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/paraview \
        -DOSPRAY_INSTALL_DIR=/opt/paraview \
        -DPARAVIEW_ENABLE_FFMPEG=ON \
        -DPARAVIEW_ENABLE_MATPLOTLIB=ON \
        -DPARAVIEW_ENABLE_PYTHON=ON \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES=ON \
        -DPARAVIEW_USE_MPI=ON \
        -DPARAVIEW_USE_VISITBRIDGE=ON \
        -DPARAVIEW_USE_OSPRAY=ON \
        -DVISIT_BUILD_READER_CGNS=ON \
        -DVTK_PYTHON_FULL_THREADSAFE=ON \
        -DVTK_PYTHON_VERSION=3 \
        -DVTK_SMP_IMPLEMENTATION_TYPE=TBB \
        ${VTK_USE_SYSTEM_LIB} \
        -GNinja

    ninja ${MAKEFLAGS}
}

package() {
    cd build

    DESTDIR="${pkgdir}" ninja install

    # Install license
    install -Dm644 "${srcdir}"/ParaView-v${pkgver}/License_v1.2.txt "${pkgdir}"/usr/share/licenses/paraview/LICENSE

    # Remove IceT man pages to avoid conflicts
    #rm -- "${pkgdir}"/usr/share/man/man3/icet*.3
    #rmdir "${pkgdir}"/usr/share/man/{man3/,}

    # add paraview to PATH
    install -Dm 755 ../paraview.sh -t "${pkgdir}/etc/profile.d"
}

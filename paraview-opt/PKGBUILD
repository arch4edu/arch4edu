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
pkgver=5.7.0
pkgrel=1
pkgdesc="Parallel Visualization application using VTK (${_mpi} version): installed to /opt/"
arch=(x86_64)
provides=(${_pkg})
conflicts=(${_pkg})
url="https://www.paraview.org"
license=(BSD custom)
depends=(boost-libs qt5-tools qt5-x11extras intel-tbb openmpi ffmpeg ospray
         python-numpy cgns protobuf
         double-conversion expat freetype2 gdal glew hdf5 libjpeg jsoncpp
         libjsoncpp.so libxml2 lz4 xz python-mpi4py netcdf libogg libpng pdal
         proj pugixml libtheora libtiff zlib)
#        gl2ps
#        libharu
#        sqlite apparently not used in this VTK configuration
optdepends=(python-matplotlib)
makedepends=(cmake boost mesa gcc-fortran ninja qt5-tools qt5-xmlpatterns eigen pegtl utf8cpp)
source=("${url}/files/v${pkgver:0:3}/ParaView-v${pkgver}.tar.xz"
        paraview-system-pugixml.patch
        vtk-python-3.8.patch::"https://gitlab.kitware.com/vtk/vtk/merge_requests/5883.patch")
source+=(paraview.sh)
sha256sums=('e41e597e1be462974a03031380d9e5ba9a7efcdb22e4ca2f3fec50361f310874'
            'dd2e23298ab5a07da0e799c3db313ed3f9d2a403d7228d50748206b535b6f65f'
            '3beff972e7e9236f2e8ab596be8f893ae7e9346a140c4538d9e8d88c3378b916')
sha256sums+=('ed1d597139473f24441e5c10038e988d64ab1d904e0c5ecaf24069734989bff4')

prepare() {
    mkdir -p build
    patch -Np0 -i ${srcdir}/paraview-system-pugixml.patch
    patch -d ParaView-v${pkgver}/VTK -p1 -i "$srcdir"/vtk-python-3.8.patch # Fix build with python 3.8 
}

build() {
    cd build

    # Flags to enable system libs in VTK building, as in VTK package
    # GL2PS has non-upstreamed patches
    # KISSFFT is not packaged
    # VERDICT is not packaged
    # ZFP is not packaged
    # LIBHARU blocked by https://github.com/libharu/libharu/pull/157
    # SQLITE apparently not used in this VTK configuration
    local VTK_USE_SYSTEM_LIB=""
    for lib in doubleconversion eigen expat freetype glew hdf5 jpeg jsoncpp libproj libxml2 lz4 lzma mpi4py netcdf ogg pegtl png pugixml theora tiff utf8 zlib
    do
        VTK_USE_SYSTEM_LIB+="-DVTK_MODULE_USE_EXTERNAL_vtk${lib}:BOOL=ON -DVTK_MODULE_USE_EXTERNAL_VTK_${lib}:BOOL=ON "
    done
    # Specific system libs for ParaView version
    for lib in cgns protobuf
    do
        VTK_USE_SYSTEM_LIB+="-DVTK_MODULE_USE_EXTERNAL_ParaView_${lib}:BOOL=ON "
    done

    cmake ../ParaView-v${pkgver} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/paraview \
        -DOSPRAY_INSTALL_DIR=/opt/paraview \
        -DPARAVIEW_ENABLE_FFMPEG=ON \
        -DPARAVIEW_ENABLE_GDAL=ON \
        -DPARAVIEW_ENABLE_PDAL=ON \
        -DPARAVIEW_ENABLE_PYTHON=ON \
        -DPARAVIEW_ENABLE_VISITBRIDGE=ON \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES=ON \
        -DPARAVIEW_USE_MPI=ON \
        -DPARAVIEW_USE_RAYTRACING=ON \
        -DVTK_ENABLE_OSPRAY=ON \
        -DVTK_PYTHON_FULL_THREADSAFE=ON \
        -DVTK_PYTHON_VERSION=3 \
        -DVTK_SMP_IMPLEMENTATION_TYPE=TBB \
        -DVTKm_ENABLE_MPI=ON \
        -DVTKm_ENABLE_RENDERING=ON \
        -DVTKm_USE_DOUBLE_PRECISION=ON \
        -DVTK_MODULE_ENABLE_VTK_GeovisCore=YES \
        -DVTK_MODULE_ENABLE_VTK_GeovisGDAL=YES \
        -DVTK_MODULE_ENABLE_VTK_IOGDAL=YES \
        -DVTK_MODULE_ENABLE_VTK_IOPDAL=YES \
        ${VTK_USE_SYSTEM_LIB} \
        -GNinja

    ninja ${MAKEFLAGS}
}

package() {
    cd build

    DESTDIR="${pkgdir}" ninja install

    # Install license
    install -Dm644 "${srcdir}"/ParaView-v${pkgver}/License_v1.2.txt "${pkgdir}"/usr/share/licenses/paraview/LICENSE

    # add paraview to PATH
    install -Dm 755 ../paraview.sh -t "${pkgdir}/etc/profile.d"
}

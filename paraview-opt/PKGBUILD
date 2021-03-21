# Maintainer: bartus <arch-user-repoᘓbartus.33mail.com>
# Maintainer: Bruno Pagani <archange@archlinux.org>
# Maintainer: Mathieu Westphal <mathieu.westphal@kitware.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: <xantares09@hotmail.com>
# shellcheck disable=SC2034,SC2154,SC2164

_pkg=paraview
_mpi=openmpi
pkgname=${_pkg}-opt
#-${_mpi}
pkgver=5.9.0
pkgrel=1
pkgdesc="Parallel Visualization application using VTK (${_mpi} version): installed to /opt/"
arch=(x86_64)
provides=("${_pkg}")
conflicts=("${_pkg}")
url="https://www.paraview.org"
license=(BSD custom)
depends=(boost-libs qt5-tools qt5-x11extras qt5-svg intel-tbb openmpi ffmpeg
         ospray python-numpy cgns protobuf
         double-conversion expat freetype2 gdal gl2ps glew hdf5 libjpeg jsoncpp
         libjsoncpp.so libharu libxml2 lz4 xz python-mpi4py netcdf libogg
         libpng pdal pugixml libtheora libtiff zlib)
optdepends=(python-matplotlib python-pandas)
makedepends=(cmake boost mesa gcc-fortran ninja qt5-tools qt5-xmlpatterns eigen utf8cpp)
# pegtl https://gitlab.kitware.com/vtk/vtk/-/issues/18151
source=(${url}/files/v${pkgver:0:3}/ParaView-v${pkgver/R/-R}.tar.xz
        paraview.sh)
sha256sums=('b03258b7cddb77f0ee142e3e77b377e5b1f503bcabc02bfa578298c99a06980d'
            '862e79bdf72f5c3ec55d3373fc34d0e5da33b1597c54c4586bdf84641d0cc291')

prepare() {
    cd ParaView-v${pkgver/R/-R}
    # We have a patched libharu
    sed -i "s|2.4.0|2.3.0|" VTK/ThirdParty/libharu/CMakeLists.txt
}

build() {
    cmake -B build -S ParaView-v${pkgver/R/-R} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/paraview \
        -DPARAVIEW_ENABLE_FFMPEG=ON \
        -DPARAVIEW_ENABLE_GDAL=ON \
        -DPARAVIEW_ENABLE_MOTIONFX=ON \
        -DPARAVIEW_ENABLE_PDAL=ON \
        -DPARAVIEW_ENABLE_RAYTRACING=ON \
        -DPARAVIEW_ENABLE_VISITBRIDGE=ON \
        -DPARAVIEW_ENABLE_XDMF3=ON \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES=ON \
        -DPARAVIEW_USE_MPI=ON \
        -DPARAVIEW_USE_PYTHON=ON \
        -DPARAVIEW_BUILD_WITH_EXTERNAL=ON \
        -DVTK_SMP_IMPLEMENTATION_TYPE=TBB \
        -DVTKm_ENABLE_MPI=ON \
        -DVTK_MODULE_ENABLE_VTK_IOGDAL=YES \
        -DVTK_MODULE_ENABLE_VTK_IOPDAL=YES \
        -DVTK_MODULE_USE_EXTERNAL_VTK_pegtl=OFF \
        -GNinja
    export NINJA_STATUS="[%p | %f<%r<%u | %cbps ] "
  # shellcheck disable=SC2086 # to allowing MAKEFLAGS to expand into multiple flags.
    ninja -C build ${MAKEFLAGS:--j1}
}

package() {
    DESTDIR="${pkgdir}" ninja -C build install

    # add paraview to PATH
    install -Dm755 paraview.sh -t "${pkgdir}"/etc/profile.d

    # Install licenses,shortcuts,icons
    install -dm755 "${pkgdir}"/usr/share
    mv "${pkgdir}"/{opt/paraview,usr}/share/licenses
    mv "${pkgdir}"/usr/share/licenses/{ParaView,paraview-opt}
    mv "${pkgdir}"/{opt/paraview,usr}/share/applications
    mv "${pkgdir}"/{opt/paraview,usr}/share/icons
}
# vim:set sw=2 ts=2 et:

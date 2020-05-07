# Maintainer : bartus <arch-user-repoᘓbartus.33mail.com>
# Maintainer: Bruno Pagani <archange@archlinux.org>
# Maintainer: Mathieu Westphal <mathieu.westphal@kitware.com>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: <xantares09@hotmail.com>
# shellcheck disable=SC2034,SC2154,SC2164

_pkg=paraview
_mpi=openmpi
pkgname=${_pkg}-opt
#-${_mpi}
pkgver=5.8.0
pkgrel=3
pkgdesc="Parallel Visualization application using VTK (${_mpi} version): installed to /opt/"
arch=(x86_64)
provides=("${_pkg}")
conflicts=("${_pkg}")
url="https://www.paraview.org"
license=(BSD custom)
depends=(boost-libs qt5-tools qt5-x11extras qt5-svg intel-tbb openmpi ffmpeg
         ospray python-numpy cgns protobuf
         double-conversion expat freetype2 gdal glew hdf5 libjpeg jsoncpp
         libjsoncpp.so libxml2 lz4 xz python-mpi4py netcdf libogg libpng pdal
         pugixml libtheora libtiff zlib)
#        gl2ps
#        libharu
optdepends=(python-matplotlib)
makedepends=(cmake boost mesa gcc-fortran ninja qt5-tools qt5-xmlpatterns eigen pegtl utf8cpp)
source=("${url}/files/v${pkgver:0:3}/ParaView-v${pkgver/R/-R}.tar.xz"
        paraview-cgns-4.1.patch::https://gitlab.kitware.com/paraview/paraview/-/commit/3d48a287141eb911b4888440e09c262743b4db3c.patch
        paraview.sh)
sha256sums=('219e4107abf40317ce054408e9c3b22fb935d464238c1c00c0161f1c8697a3f9'
            '785cb6bd349608f441ec90ac0bd3059efc3a14856c3513733729605ee240cf90'
            '862e79bdf72f5c3ec55d3373fc34d0e5da33b1597c54c4586bdf84641d0cc291')

prepare() {
    cd ParaView-v${pkgver/R/-R}
    patch -p1 -i ../paraview-cgns-4.1.patch
}

build() {
    # Note regarding use of system dependencies:
    # GL2PS has non-upstreamed patches
    # LIBHARU blocked by https://github.com/libharu/libharu/pull/157
    cmake -B build -S ParaView-v${pkgver/R/-R} -GNinja \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/opt/paraview \
        -DPARAVIEW_ENABLE_FFMPEG=ON \
        -DPARAVIEW_ENABLE_GDAL=ON \
        -DPARAVIEW_ENABLE_MOTIONFX=ON \
        -DPARAVIEW_ENABLE_PDAL=ON \
        -DPARAVIEW_ENABLE_VISITBRIDGE=ON \
        -DPARAVIEW_ENABLE_XDMF3=ON \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES=ON \
        -DPARAVIEW_USE_MPI=ON \
        -DPARAVIEW_USE_PYTHON=ON \
        -DPARAVIEW_USE_RAYTRACING=ON \
        -DPARAVIEW_BUILD_WITH_EXTERNAL=ON \
        -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=OFF \
        -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=OFF \
        -DVTK_SMP_IMPLEMENTATION_TYPE=TBB \
        -DVTKm_ENABLE_MPI=ON \
        -DVTK_MODULE_ENABLE_VTK_IOGDAL=YES \
        -DVTK_MODULE_ENABLE_VTK_IOPDAL=YES \
        -DCMAKE_C_FLAGS="-DH5_USE_110_API" \
        -DCMAKE_CXX_FLAGS="-DH5_USE_110_API" \

    export NINJA_STATUS="[%p | %f<%r<%u | %cbps ] "
  # shellcheck disable=SC2086 # to allowing MAKEFLAGS to expand into multiple flags.
    ninja -C build ${MAKEFLAGS:--j1}
}

package() {
    DESTDIR="${pkgdir}" ninja -C build install

    # Install license
    install -Dm644 ParaView-v${pkgver/R/-R}/License_v1.2.txt "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE

    # add paraview to PATH
    install -Dm 755 paraview.sh -t "${pkgdir}/etc/profile.d"
}
# vim:set sw=2 ts=2 et:

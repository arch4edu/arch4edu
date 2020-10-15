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
pkgver=5.8.1
pkgrel=2
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
optdepends=(python-matplotlib)
makedepends=(cmake boost mesa gcc-fortran ninja qt5-tools qt5-xmlpatterns eigen pegtl utf8cpp)
source=("${url}/files/v${pkgver:0:3}/ParaView-v${pkgver/R/-R}.tar.xz"
        paraview-cgns-4.1.patch::https://gitlab.kitware.com/paraview/paraview/-/commit/3d48a287141eb911b4888440e09c262743b4db3c.patch
        paraview.sh
        paraview-vtk-freetype-2.10.3.patch)
sha256sums=('7653950392a0d7c0287c26f1d3a25cdbaa11baa7524b0af0e6a1a0d7d487d034'
            '917485fbff57b922e67e40ee35d265769b05b4b62c397e4c9ce00244f5fd07ae'
            '862e79bdf72f5c3ec55d3373fc34d0e5da33b1597c54c4586bdf84641d0cc291'
            'b547a665eaf980669b929f3a95e61cc8af4892ba3a41441ef98f8487886081ce')

prepare() {
    cd ParaView-v${pkgver/R/-R}
    patch -p1 -i ../paraview-cgns-4.1.patch
    # We have a patched libharu
    sed -i "s|2.4.0|2.3.0|" VTK/ThirdParty/libharu/CMakeLists.txt
    # https://bugs.archlinux.org/task/68244
    patch -Np1 -i ../paraview-vtk-freetype-2.10.3.patch
}

build() {
    export CPPFLAGS+=" -DH5_USE_110_API"
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

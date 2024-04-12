#!/usr/hint/bash
# Maintainer : bartus <arch-user-repoᘓbartus.33mail.com>
# shellcheck disable=SC2034,SC2154 # allow unused/uninitialized variables.

#Todo:
#* add external cmake projects to source array and patch src/externla/*.cmake
#* use system wide: levmar, libigl, structyresynth, libe57, u3d, tinygltf

#Configuration:
#Use: makepkg VAR1=0 VAR2=1 to enable(1) disable(0) a feature
#Use: {yay,paru} --mflags=VAR1=0,VAR2=1
#Use: aurutils --margs=VAR1=0,VAR2=1
#Use: VAR1=0 VAR2=1 pamac

# Use CMAKE_FLAGS=xxx:yyy:zzz to define extra CMake flags
[[ -v CMAKE_FLAGS ]] && mapfile -t -d: _cmake_flags < <(echo -n "$CMAKE_FLAGS")

pkgname=meshlab
pkgver=2023.12
_pkgver_vcg=${pkgver}
pkgrel=4
pkgdesc="System for processing and editing of unstructured 3D models arising in 3D scanning (qt5 version)"
arch=('i686' 'x86_64')
url="https://www.meshlab.net"
license=('GPL2')
depends=('bzip2' 'cgal' 'glew' 'glu' 'openssl' 'qt5-base' 'qt5-declarative' 'qt5-script' 'qt5-xmlpatterns' 'xerces-c'
         'gmp' 'mpfr' 'mesa' 'qhull')
makedepends=('boost' 'cmake' 'eigen' 'ninja' 'git' 'muparser' 'lib3ds' 'openctm-tools' 'patchelf')
optdepends=('lib3ds: for Autodesk`s 3D-Studio r3 and r4 .3DS file support'
            'muparser: for filer_func plugins'
            'openctm-tools: for compressed triangle mesh file format')
source=("$pkgname::git+https://github.com/cnr-isti-vclab/meshlab.git#tag=MeshLab-${pkgver}"
        "vcglib::git+https://github.com/cnr-isti-vclab/vcglib.git#tag=${_pkgver_vcg}"
        )
sha256sums=('SKIP'
            'SKIP')

prepare() {
  prepare_submodule
}


build() {
  _cmake_flags+=( '-DCMAKE_INSTALL_PREFIX=/usr'
                  '-DCMAKE_BUILD_TYPE=Release'
                  '-DCMAKE_C_COMPILER=gcc'
                  '-DCMAKE_CXX_COMPILER=g++'
                )
  cmake "${_cmake_flags[@]}" -G Ninja -B "${srcdir}/build" -S "${srcdir}/meshlab"
# Fix gcc:13 build
  sed -i '1 i\#include <cstdint>' "${srcdir}"/meshlab/src/external/downloads/{nexus-master/src/corto/include/corto/tunstall.h,libE57Format-2.3.0/include/E57Format.h}
# shellcheck disable=SC2046 # allow MAKEFLAGS to split when passing multiple flags.
 ninja $(grep -oP -- '-+[A-z]+ ?[0-9]*'<<<"${MAKEFLAGS:--j1}") -C "${srcdir}/build"
}

package() {
  DESTDIR="$pkgdir" ninja -C "${srcdir}/build" install
  # Fix libio_u3d.so missing rpath
  patchelf --set-rpath '$ORIGIN/../' ${pkgdir}/usr/lib/meshlab/plugins/libio_u3d.so
}

# Generated with git_submodule_PKGBUILD_conf.sh ( https://gist.github.com/bartoszek/41a3bfb707f1b258de061f75b109042b )
# Call prepare_submodule in prepare() function

prepare_submodule() {
  git -C "$srcdir/meshlab" config submodule.src/vcglib.url "$srcdir/vcglib"
  git -C "$srcdir/meshlab" -c protocol.file.allow=always submodule update --init
}

# vim:set ts=2 sw=2 et:

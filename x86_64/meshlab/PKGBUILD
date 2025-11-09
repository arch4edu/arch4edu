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

# cherry pick commits form current master
_backports=(
903434699 # add cmake minimum policy for qhull
be26273c9 # add cmake minimum policy for nexus
13de6ebbd # add cmake minimum policy for levmar
61823b4b8 # update embree to 4.3.3
#0e9aafb19 # update vcg submodule
)

pkgname=meshlab
pkgver=2025.07
pkgrel=2
pkgdesc="System for processing and editing of unstructured 3D models arising in 3D scanning (qt5 version)"
arch=('i686' 'x86_64')
url="https://www.meshlab.net"
license=('GPL2')
depends=('bzip2' 'cgal' 'embree' 'glew' 'glu' 'openssl' 'qt5-base' 'qt5-declarative' 'qt5-script' 'qt5-xmlpatterns' 'xerces-c'
         'gmp' 'mpfr' 'mesa' 'qhull')
makedepends=('boost' 'cmake' 'eigen' 'ninja' 'git' 'muparser' 'lib3ds' 'openctm-tools' 'patchelf')
optdepends=('lib3ds: for Autodesk`s 3D-Studio r3 and r4 .3DS file support'
            'muparser: for filer_func plugins'
            'openctm-tools: for compressed triangle mesh file format')
source=("$pkgname::git+https://github.com/cnr-isti-vclab/meshlab.git#tag=MeshLab-${pkgver}"
        lib3mf.patch
        )
sha256sums=('c9df509edc216bf2876ddee3be2b6624e685ae546a00a6f05caef29f3f986c3a'
            '41fdc7c5ecab23a7b161e1aba2001ffdae713bbb13188b9bbc170c1dea959408')

prepare() {
  git -C "$srcdir/meshlab" cherry-pick -v -n "${_backports[@]}"
  prepare_submodule
  git -C "$srcdir/meshlab" apply -v "$srcdir"/lib3mf.patch
}


build() {
  _cmake_flags+=( '-DCMAKE_INSTALL_PREFIX=/usr'
                  '-DCMAKE_BUILD_TYPE=Release'
                  '-DCMAKE_C_COMPILER=gcc'
                  '-DCMAKE_CXX_COMPILER=g++'
                )
  cmake "${_cmake_flags[@]}" -G Ninja -B "${srcdir}/build" -S "${srcdir}/meshlab"
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
  git -C "$srcdir/meshlab" -c protocol.file.allow=always submodule update --init
}

# vim:set ts=2 sw=2 et:

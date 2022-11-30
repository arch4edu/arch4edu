#!/usr/hint/bash
# Maintainer : bartus <arch-user-repoᘓbartus.33mail.com>
# shellcheck disable=SC2034,SC2154 # allow unused/uninitialized variables.

#Configuration:
#Use: makepkg VAR1=0 VAR2=1 to enable(1) disable(0) a feature
#Use: {yay,paru} --mflags=VAR1=0,VAR2=1
#Use: aurutils --margs=VAR1=0,VAR2=1
#Use: VAR1=0 VAR2=1 pamac

# Use CMAKE_FLAGS=xxx:yyy:zzz to define extra CMake flags
[[ -v CMAKE_FLAGS ]] && mapfile -t -d: _cmake_flags < <(echo -n "$CMAKE_FLAGS")

pkgname=meshlab
pkgver=2022.02
_pkgver_vcg=${pkgver}
pkgrel=1
pkgdesc="System for processing and editing of unstructured 3D models arising in 3D scanning (qt5 version)"
arch=('i686' 'x86_64')
url="https://www.meshlab.net"
license=('GPL2')
depends=('bzip2' 'cgal' 'glew' 'glu' 'openssl-1.0' 'qt5-base' 'qt5-declarative' 'qt5-script' 'qt5-xmlpatterns' 'xerces-c')
makedepends=('boost' 'cmake' 'eigen' 'ninja' 'git' 'muparser' 'levmar' 'lib3ds' 'mpir' 'openctm-tools')
optdepends=('u3d: for U3D and IDTF file support'
            'lib3ds: for Autodesk`s 3D-Studio r3 and r4 .3DS file support'
            'levmar: for isoparametrization and mutualcorrs plugins'
            'muparser: for filer_func plugins'
            'mpir: for Constructive Solid Geometry operation filters'
            'openctm-tools: for compressed triangle mesh file format')
#also create openctm(aur) jhead-lib structuresynth-lib to handle last dep
source=("$pkgname::git+https://github.com/cnr-isti-vclab/meshlab.git#tag=MeshLab-${pkgver}"
        "vcglib::git+https://github.com/cnr-isti-vclab/vcglib.git#tag=${_pkgver_vcg}"
        )
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
  prepare_submodule
}


build() {
  _cmake_flags=( '-DALLOW_SYSTEM_QHULL=OFF'
                 '-DCMAKE_INSTALL_PREFIX=/usr'
                 '-DCMAKE_BUILD_TYPE=Release'
               )
  cmake "${_cmake_flags[@]}" -G Ninja -B "${srcdir}/build" -S "${srcdir}/meshlab/src"
# shellcheck disable=SC2046 # allow MAKEFLAGS to split when passing multiple flags.
 ninja $(grep -oP -- '-+[A-z]+ ?[0-9]*'<<<"${MAKEFLAGS:--j1}") -C "${srcdir}/build"
}

package() {
  DESTDIR="$pkgdir" ninja -C "${srcdir}/build" install
}

# Generated with git_submodule_PKGBUILD_conf.sh ( https://gist.github.com/bartoszek/41a3bfb707f1b258de061f75b109042b )
# Call prepare_submodule in prepare() function

prepare_submodule() {
  git -C "$srcdir/meshlab" config submodule.src/vcglib.url "$srcdir/vcglib"
  git -C "$srcdir/meshlab" config submodule.src/external/nexus.url "$srcdir/nexus"
  git -C "$srcdir/meshlab" -c protocol.file.allow=always submodule update --init
  git -C "$srcdir/meshlab/src/external/nexus" config submodule.src/corto.url "$srcdir/corto"
  git -C "$srcdir/meshlab/src/external/nexus" -c protocol.file.allow=always submodule update --init
}
source+=(
# "vcglib::git+https://github.com/cnr-isti-vclab/vcglib.git"
  "nexus::git+https://github.com/cnr-isti-vclab/nexus.git"
  "corto::git+https://github.com/cnr-isti-vclab/corto.git"
)

# vim:set ts=2 sw=2 et:

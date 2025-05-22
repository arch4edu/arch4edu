# Maintainer: envolution
# Contributor: Jed Brown <jed@59A2.org>
# Contributor: George Eleftheriou <eleftg>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=parmetis
pkgver=4.0.3+p7
_pkgver=${pkgver%%+*}
_debver=${pkgver/+p/-}
pkgrel=1
epoch=1
pkgdesc="A parallel graph partitioning library (debian patches)"
url="http://glaros.dtc.umn.edu/gkhome/metis/parmetis/overview"
#debian url=https://salsa.debian.org/science-team/parmetis
arch=('i686' 'x86_64')
license=(LicenseRef-custom)
depends=(openmpi metis gklib glibc)
makedepends=(cmake)
source=(
  http://deb.debian.org/debian/pool/non-free/p/parmetis/parmetis_${_pkgver}.orig.tar.gz
  http://deb.debian.org/debian/pool/non-free/p/parmetis/parmetis_${_debver}.debian.tar.xz
)
sha256sums=('f2d9a231b7cf97f1fee6e8c9663113ebf6c240d407d3c118c55b3633d6be6e5f'
            '0f2130dd5c6a7b2df5214b795eb51df2cc71c43e1194a117150297cec85b93b6')

prepare() {
  cd ${pkgname}-${_pkgver}
  # Apply Debian patches using the series file
  if [[ -f "../debian/patches/series" ]]; then
    while read -r patch; do
      [[ -z $patch || $patch == \#* ]] && continue
      patch -Np1 <"../debian/patches/${patch}" || return 1
    done <"../debian/patches/series"
  else
    echo "Warning: patches/series file not found, skipping patching"
  fi

  _cmake_flags=(
    -DCMAKE_SHARED_LINKER_FLAGS="-lGKlib -Wl,-z,relro,-z,now"
    -DCMAKE_EXE_LINKER_FLAGS="-lGKlib -Wl,-z,relro,-z,now"
    -DCMAKE_SKIP_RPATH=ON
  )
  sed -i "s|^CONFIG_FLAGS = .*|CONFIG_FLAGS = ${_cmake_flags[*]}|" Makefile
  sed -i 's|^cmake_minimum.*|cmake_minimum_required(VERSION 4.0)|' CMakeLists.txt
  make config shared=1 prefix=/usr
}
build() {
  cd ${pkgname}-${_pkgver}
  make
}

package() {
  cd ${pkgname}-${_pkgver}
  make install "DESTDIR=$pkgdir"
  install -Dm644 LICENSE.txt -t $pkgdir/usr/share/licenses/$pkgname
  install -Dm644 metis/LICENSE.txt $pkgdir/usr/share/licenses/$pkgname/metis-LICENSE.txt

}
# vim:set ts=2 sw=2 et:

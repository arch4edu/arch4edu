# Contributor: Max Devaine <max@devaine.cz>
# Maintainer: acxz <akashpatel2008 at yahoo dot com>
pkgname=code-eli-git
pkgver=r821.f9ff74f
pkgrel=3
pkgdesc='Collection of C++ libraries that provide a variety of functionalities.'
arch=('i686' 'x86_64')
url='https://github.com/ramcdona/Code-Eli'
license=('EPL 1.0')
depends=('eigen')
optdepends=('cpptest: unit tests'
            'doxygen: documentation')
makedepends=('cmake' 'git')
_name=Code-Eli
provides=('code-eli')
source=("git+https://github.com/ramcdona/Code-Eli.git")
md5sums=('SKIP')

pkgver() {
  cd "$_name"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

_buildtype="Release"

build() {

  # Create a build directory
  mkdir -p "${srcdir}/${_name}/build"
  cd "${srcdir}/${_name}/build"

  msg "Starting CMake (build type: ${_buildtype})"

  cmake .. \
    -DCMAKE_BUILD_TYPE=${_buildtype} \
    -DCMAKE_INSTALL_PREFIX='/usr'

  msg "Building the project"
  make

}

package() {

  cd "${srcdir}/${_name}"

  msg "Installing files"

  mkdir -p "${pkgdir}/usr/include/eli"
  # include
  cp -r include/eli/* ${pkgdir}/usr/include/eli

  cd "${srcdir}/${_name}/build"
  cp -r include/eli/* ${pkgdir}/usr/include/eli

}

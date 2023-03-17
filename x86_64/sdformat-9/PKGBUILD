# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Nxxx <nx dot tardis at gmail dot com>

pkgname=sdformat-9
pkgver=9.8.0
pkgrel=3
pkgdesc="SDF Converter for gazebo"
arch=('i686' 'x86_64')
url="http://sdformat.org/"
license=('Apache')
depends=('boost' 'tinyxml' 'ignition-math=6' 'python-psutil' 'urdfdom')
makedepends=('cmake' 'doxygen' 'ignition-cmake=2' 'ignition-tools=1' 'ruby' 'ruby-rexml')
provides=('sdformat=9')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/osrf/sdformat/archive/sdformat9_${pkgver}.tar.gz")
sha256sums=('6aabb4e08073d506f27a8e801eb175cca9a1c938e4fbff6b30f0b2ddf52a9b5e')

_dir="sdformat-sdformat9_${pkgver}"

build() {
  cd "${srcdir}/${_dir}"
  mkdir -p build && cd build

  cmake .. -DCMAKE_BUILD_TYPE="Release" \
           -DCMAKE_INSTALL_PREFIX=/usr \
           -DCMAKE_INSTALL_LIBDIR=lib

  make
}

package() {
  cd "${srcdir}/${_dir}/build"
  make DESTDIR="$pkgdir/" install
}

# Maintainer:  <gucong43216@gmail.com>

pkgname=ospray
pkgver=1.2.1
pkgrel=1
pkgdesc="A Ray Tracing Based Rendering Engine for High-Fidelity Visualization"
arch=('i686' 'x86_64')
url="http://www.ospray.org/"
license=('Apache')
depends=('qt4>=4.6' 'ispc' 'intel-tbb' 'embree-isa' 'libgl' 'freeglut' 'glu' 'imagemagick')
makedepends=('cmake')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ospray/OSPRay/archive/v$pkgver.tar.gz")
md5sums=('37f9d7f59174d645a78da95f223cc118')

prepare() {
  cd "$srcdir"

  [[ -d ${pkgname}-build ]] && rm -r ${pkgname}-build
  mkdir ${pkgname}-build

}

build() {
  cd "$srcdir/${pkgname}-build"

  export embree_DIR=/usr

  # MAX_ISA is detected in aur/embree-isa in build-time
  # Building may fail with community/embree
  cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib \
        -DOSPRAY_USE_EXTERNAL_EMBREE:BOOL=ON \
        -DUSE_IMAGE_MAGICK:BOOL=ON \
        ../${pkgname}-${pkgver}
  make
}

package() {
  cd "$srcdir/${pkgname}-build"

  make DESTDIR="$pkgdir" install
}

# vim:set ts=2 sw=2 et:

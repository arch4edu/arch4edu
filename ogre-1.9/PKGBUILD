# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Firas Zaidan <firas@zaidan.de>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
pkgbase=ogre-1.9
pkgname=('ogre-1.9' 'ogre-docs-1.9')
pkgver=1.9.1
pkgrel=3
pkgdesc='Scene-oriented, flexible 3D engine written in C++'
arch=('x86_64')
url='http://www.ogre3d.org'
license=('custom:MIT')
depends=('freeimage' 'freetype2' 'libxaw' 'libxrandr' 'openexr'
         'nvidia-cg-toolkit' 'zziplib' 'sdl2' 'glu' 'tinyxml')
makedepends=('cmake' 'doxygen' 'graphviz' 'ttf-dejavu' 'mesa' 'python' 'swig' 'systemd')
provides=('ogre=1.9' 'ogre-docs=1.9')
source=("https://github.com/OGRECave/ogre/archive/v${pkgver}.tar.gz")
sha512sums=('69e1ea27ef3126ac0e09be9c1f8a9fc762630cd236ce6c3352a550ad977925387b1dfb9d124cc27bb8ac5231e036155451db988a26de6fb2df6da6f7d961115d')

prepare() {
  mkdir -p ogre-${pkgver}/build
}

build() {
  cd ogre-${pkgver}/build

  cmake .. \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DOGRE_BUILD_DEPENDENCIES=FALSE \
    -DCMAKE_BUILD_TYPE=Release \
    -DOGRE_BUILD_PLUGIN_FREEIMAGE=TRUE \
    -DOGRE_BUILD_PLUGIN_EXRCODEC=TRUE \
    -DOGRE_INSTALL_SAMPLES=TRUE \
    -DOGRE_INSTALL_SAMPLES_SOURCE=TRUE

  make
  make OgreDoc
}

package_ogre-1.9() {
  optdepends=('cppunit: unit testing'
              'python: python bindings'
              'ogre-docs: documentation')

  cd ogre-${pkgver}/build

  make DESTDIR=${pkgdir} install

  install -Dm644 ../Docs/License.html ${pkgdir}/usr/share/licenses/${pkgname}/license.html

  # move docs out of this package
  mv ${pkgdir}/usr/share/OGRE/docs ${srcdir}/docs
}

package_ogre-docs-1.9() {
  pkgdesc="Documentation for ogre"
  depends=()

  cd ogre-${pkgver}/build

  # move docs into this package
  install -dm755 ${pkgdir}/usr/share/doc
  mv ${srcdir}/docs ${pkgdir}/usr/share/doc/OGRE/

  # symlink for docs
  install -dm755 ${pkgdir}/usr/share/OGRE/
  cd ${pkgdir}/usr/share
  ln -s /usr/share/doc/OGRE/ OGRE/docs
}

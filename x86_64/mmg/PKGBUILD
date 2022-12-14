# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mmg
pkgver=5.7.0
pkgrel=1
pkgdesc='Anisotropic tetrahedral remesher and moving mesh generator'
url="http://www.mmgtools.org/"
license=('GPL')
arch=('i686' 'x86_64')
depends=('scotch' 'vtk' 'pugixml')
makedepends=('cmake' 'netcdf' 'proj' 'qt5-base' 'glew' 'python' 'libogg' 'libtheora' 'fmt' 'tbb')
provides=('mmg3d')
conflicts=('mmg3d')
replaces=('mmg3d')
source=("$pkgname-$pkgver.tar.gz::https://github.com/MmgTools/mmg/archive/v$pkgver.tar.gz")
sha256sums=('6265a347e5e1148b0515f73c6f30c8e37763195e5483ab7d691cd59f70cfe7fb')

build () {
  cmake -S "$srcdir/$pkgname-$pkgver" -B build \
    -DCMAKE_INSTALL_PREFIX="$pkgdir"/usr \
    -DBUILD_SHARED_LIBS=ON \
    -DUSE_ELAS=OFF \
    -DUSE_VTK=ON

  cmake --build build
}

package() {
  touch "$srcdir"/$pkgname-$pkgver/libmmgf.h
  cmake --install build
}

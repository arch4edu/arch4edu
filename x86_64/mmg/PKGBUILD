# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mmg
pkgver=5.7.1
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
sha256sums=('27c09477ebc080f54919f76f8533a343936677c81809fe37ce4e2d62fa97237b')

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

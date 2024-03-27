# Maintainer: Gianluca Pettinello <g_pet@hotmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mmg
pkgver=5.7.2
pkgrel=1
pkgdesc='Anisotropic tetrahedral remesher and moving mesh generator'
url="http://www.mmgtools.org/"
license=('GPL')
arch=('i686' 'x86_64')
depends=('scotch' 'vtk' 'pugixml' 'python-mpi4py')
makedepends=('cmake' 'netcdf' 'proj' 'qt6-base' 'glew' 'python' 'libogg' 'libtheora' 'fmt' 'onetbb')
provides=('mmg3d')
conflicts=('mmg3d')
replaces=('mmg3d')
source=("$pkgname-$pkgver.tar.gz::https://github.com/MmgTools/mmg/archive/v$pkgver.tar.gz")
sha256sums=('4c396dd44aec69e0a171a04f857e28aad2e0bbfb733b48b6d81a2c6868e86840')

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

# Maintainer: Gianluca Pettinello <g_pet@hotmail.com>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mmg
pkgver=5.8.0
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
sha256sums=('686eaab84de79c072f3aedf26cd11ced44c84b435d51ce34e016ad203172922f')

build() {
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

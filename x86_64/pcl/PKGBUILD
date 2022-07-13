# Maintainer: Benjamin Chrétien <chretien dot b plus aur at gmail dot com>
# Contributor: Fabio Loli <loli_fabio@protonmail.com>
# Contributor: Yuxin Wu <ppwwyyxxc@gmail.com>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
# Contributor: hauptmech
# Contributor: figo.zhang
# Contributor: lubosz
# Contributor: ZiXiS

pkgname=pcl
pkgver=1.12.1
pkgrel=2
pkgdesc="A comprehensive open source library for n-D Point Clouds and 3D geometry processing"
arch=('x86_64' 'i686')
url='http://www.pointclouds.org'
license=('BSD')
depends=('boost' 'eigen' 'flann' 'vtk' 'qhull' 'qt5-base' 'glu' 'qt5-webkit'
  'openmpi' 'python' 'libxt' 'libharu' 'proj' 'glew' 'netcdf' 'libusb' 'fmt' 
  'pugixml' 'liblas' 'adios2' 'utf8cpp' 'freeglut' 'ospray' 'python-mpi4py' 'openvr' 'cgns'
  'unixodbc' 'openni2' 'libxcursor')
makedepends=('cmake' 'gl2ps' 'python')
optdepends=('cuda' 'openni2' 'python-sphinx')
source=("pcl-${pkgver}.tar.gz"::"https://github.com/PointCloudLibrary/pcl/archive/pcl-${pkgver}.tar.gz")

sha256sums=('dc0ac26f094eafa7b26c3653838494cc0a012bd1bdc1f1b0dc79b16c2de0125a' )

build() {
 # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  cmake ${srcdir}/pcl-pcl-${pkgver} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_surface_on_nurbs=ON \
    -DCMAKE_CXX_STANDARD=14 \
    -DCUDA_HOST_COMPILER=/usr/bin/gcc

  make 
}

package() {
  cd "${srcdir}/build"
  make DESTDIR=${pkgdir} install

  install -Dm644 ${srcdir}/pcl-pcl-${pkgver}/LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

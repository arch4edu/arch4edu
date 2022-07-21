# Contributor: dtag <dtag00@gmail.com>

pkgname=ceres-solver
pkgver=2.1.0
pkgrel=1
pkgdesc="Solver for nonlinear least squares problems"
arch=('i686' 'x86_64')
url="http://ceres-solver.org/"
license=('LGPL')
makedepends=('cmake')
depends=('google-glog>=0.3.5' 'eigen>=3.3.0'
      'suitesparse>=4.4.5')
optdepends=('openmp')
source=("http://ceres-solver.org/ceres-solver-2.1.0.tar.gz")
sha256sums=('f7d74eecde0aed75bfc51ec48c91d01fe16a6bf16bce1987a7073286701e2fc6')
options=('staticlibs')

_cmakeopts=('-D CMAKE_BUILD_TYPE=Release'
            '-D CMAKE_INSTALL_PREFIX=/usr'
            '-D EIGENSPARSE=ON'
            '-D BUILD_SHARED_LIBS=ON'
            '-D BUILD_TESTING=OFF'
            '-D BUILD_EXAMPLES=OFF'
            '-D BUILD_BENCHMARKS=OFF')

build() {
  cd $srcdir/$pkgname-$pkgver
  mkdir -p ./build
  cd ./build
  cmake ${_cmakeopts[@]} ../
  make
}

package ()
{
  cd $srcdir/$pkgname-$pkgver/build/
  make DESTDIR=$pkgdir install
  install -Dm644 ../LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Pin Eigen version preventing version mismatch cmake config after Eigen update.
  index=$(declare -p depends | sed -n "s,.*\[\([^]]*\)\]=\"eigen.*\".*,\1,p")
  depends[$index]=$(pacman -Sp --print-format "%n=%v" eigen|cut -d- -f1)
}

# Maintainer: Kartik Mohta <kartikmohta@gmail.com>
pkgname=gtsam-mkl
pkgver=4.1.1
pkgrel=1
pkgdesc="A library of C++ classes that implement smoothing and mapping (SAM) in\
  robotics and vision, using factor graphs and Bayes networks as the underlying\
  computing paradigm rather than sparse matrices."
url="https://gtsam.org/"
arch=('x86_64' 'i686')
provides=("gtsam=${pkgver}")
conflicts=('gtsam' 'gtsam-git')
license=('BSD')
depends=('boost-libs' 'eigen' 'intel-tbb' 'intel-mkl')
makedepends=('boost' 'cmake')
source=("https://github.com/borglab/gtsam/archive/${pkgver}.tar.gz")
sha256sums=('c7b5e6cdad52b141c272778f47baf628975457be3e26ed96a7bc2ae685a00af0')

build() {
  cd "${srcdir}/gtsam-${pkgver}"
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
    -DGTSAM_BUILD_DOCS=OFF \
    -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
    -DGTSAM_BUILD_TESTS=ON \
    -DGTSAM_BUILD_WITH_CCACHE=OFF \
    -DGTSAM_BUILD_WITH_MARCH_NATIVE=OFF \
    -DGTSAM_INSTALL_CPPUNITLITE=OFF \
    -DGTSAM_INSTALL_GEOGRAPHICLIB=OFF \
    -DGTSAM_USE_SYSTEM_EIGEN=ON \
    -DGTSAM_WITH_EIGEN_MKL=ON \
    ..
  make
}

package() {
  cd "${srcdir}/gtsam-${pkgver}/build"
  make DESTDIR="${pkgdir}" install
  install -Dm644 "${srcdir}/gtsam-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# check() {
#   cd "${srcdir}/${pkgname}-${pkgver}/build"
#   make check
# }

# vim:set ts=2 sw=2 et:

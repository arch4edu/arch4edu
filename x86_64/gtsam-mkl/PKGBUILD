# Maintainer: Kartik Mohta <kartikmohta@gmail.com>
pkgname=gtsam-mkl
pkgver=4.2.0
pkgrel=2
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
sha256sums=('8b44d6b98a3b608664d1c9a7c1383a406550499d894533bb0183e6cf487e6457')

build() {
  cmake -B build -S "gtsam-${pkgver}" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev \
        -DGTSAM_BUILD_DOCS=OFF \
        -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
        -DGTSAM_BUILD_TESTS=OFF \
        -DGTSAM_BUILD_WITH_CCACHE=OFF \
        -DGTSAM_BUILD_WITH_MARCH_NATIVE=OFF \
        -DGTSAM_INSTALL_CPPUNITLITE=OFF \
        -DGTSAM_INSTALL_GEOGRAPHICLIB=OFF \
        -DGTSAM_USE_SYSTEM_EIGEN=ON \
        -DGTSAM_WITH_EIGEN_MKL=ON
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "${srcdir}/gtsam-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# check() {
#   ctest --test-dir build --output-on-failure
# }

# vim:set ts=2 sw=2 et:

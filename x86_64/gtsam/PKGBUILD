# Maintainer: envolution
# Contributor: Kartik Mohta <kartikmohta@gmail.com>
# shellcheck shell=bash disable=SC2034,SC2154
pkgname=gtsam
pkgver=4.2
pkgrel=1
epoch=1
pkgdesc="A library of C++ classes that implement smoothing and mapping (SAM) in\
  robotics and vision, using factor graphs and Bayes networks as the underlying\
  computing paradigm rather than sparse matrices."
url="https://gtsam.org/"
arch=('x86_64' 'i686')
provides=("gtsam=${pkgver}")
license=('BSD-3-Clause')
depends=('boost-libs' 'eigen')
makedepends=('boost' 'cmake')
optdepends=('intel-tbb: Use Intel TBB to accelerate computations (add this to the depends section of the PKGBUILD and rebuild the package)')
source=("https://github.com/borglab/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('9ff8846d0a83a245c284cb5760ec2d74535ef9b5885183ccfefd7ff122eba60e')

build() {
  cmake -B build -S "${pkgname}-${pkgver}" \
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
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# check() {
#   ctest --test-dir build --output-on-failure
# }

# vim:set ts=2 sw=2 et:

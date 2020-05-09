# Maintainer: Kartik Mohta <kartikmohta@gmail.com>
pkgname=gtsam-mkl
pkgver=4.0.2
pkgrel=5
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
source=("https://github.com/borglab/${pkgname}/archive/${pkgver}.tar.gz"
        "rename-included-libmetis.patch"
        "skip-boost-debug-libs.patch"
        "fix-findmkl.patch")
md5sums=('fc24394cf59ccf034ae4150d8613384b'
         '63093f474f5574e8dd3e300289dab47f'
         '3df2bbd13382765fbe40f503f3a99219'
         '3ba08e16a06755c8cdf637b896d186a3')


prepare() {
  cd "${srcdir}/gtsam-${pkgver}"
  patch -p1 -i ../rename-included-libmetis.patch
  patch -p1 -i ../skip-boost-debug-libs.patch
  patch -p1 -i ../fix-findmkl.patch
}

build() {
  cd "${srcdir}/gtsam-${pkgver}"
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
    -DGTSAM_BUILD_EXAMPLES_ALWAYS=OFF \
    -DGTSAM_BUILD_TESTS=ON \
    -DGTSAM_BUILD_WRAP=OFF \
    -DGTSAM_BUILD_DOCS=OFF \
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

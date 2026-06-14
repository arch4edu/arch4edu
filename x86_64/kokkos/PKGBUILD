# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
pkgname=kokkos
pkgver=5.1.1
pkgrel=1
pkgdesc="C++ performance portability programming ecosystem"
arch=(x86_64)
url="https://github.com/${pkgname}/${pkgname}"
license=(Apache-2.0)
depends=(bash hwloc)
makedepends=(cmake)
# checkdepends=(gtest)
conflicts=('trilinos')
source=(${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha256sums=('77cbde0066f5ea9343d35be452826b6b226ceacb385239c28cc9688baf471cc0')

build() {
  cmake \
    -S ${pkgname}-${pkgver} \
    -B build \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DKokkos_ENABLE_BENCHMARKS=OFF \
    -DKokkos_ENABLE_CUDA=OFF \
    -DKokkos_ENABLE_DEBUG=OFF \
    -DKokkos_ENABLE_EXAMPLES=OFF \
    -DKokkos_ENABLE_HIP=OFF \
    -DKokkos_ENABLE_HWLOC=ON \
    -DKokkos_ENABLE_HPX=OFF \
    -DKokkos_ENABLE_LIBDL=ON \
    -DKokkos_ENABLE_ONEDPL=OFF \
    -DKokkos_ENABLE_OPENACC=OFF \
    -DKokkos_ENABLE_OPENMP=OFF \
    -DKokkos_ENABLE_ROCM=OFF \
    -DKokkos_ENABLE_SERIAL=ON \
    -DKokkos_ENABLE_SYCL=OFF \
    -DKokkos_ENABLE_TESTS=OFF \
    -DKokkos_ENABLE_THREADS=ON \
    -Wno-dev
  cmake --build build --target all
}

# check() {
#   ctest --test-dir build
# }

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  install -Dm644 ${pkgname}-${pkgver}/LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

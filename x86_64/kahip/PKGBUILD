# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.17
pkgrel=1
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=(x86_64)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmp metis openmpi python)
makedepends=(cmake pybind11)
optdepends=('gurobi: for ILP solver in ilp_improve')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c3ba72965fe3d842515813e5244dfccc469f1df4b5e6a6cfe2813fe33f4b427508b66c5c570f1c9d2e6e191f5b15d525ded6736ced132bdb5f654e301936da64')

build() {
  cmake \
    -S ${_base}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=11 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DBUILDPYTHONMODULE=ON \
    -DUSE_TCMALLOC=OFF \
    -DUSE_ILP=OFF \
    -Wno-dev
  cmake --build build --target all
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}{sys.version_info.minor}')")
  install -dm755 "${pkgdir}${site_packages}"
  mv "build/${_base,,}.cpython-${_pyversion}-${CARCH}-linux-gnu.so" "${pkgdir}${site_packages}"
  install -Dm 644 ${_base}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  find "${pkgdir}" -type d -empty -delete
}

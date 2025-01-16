# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.18
pkgrel=1
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=(x86_64)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmp metis openmpi python)
makedepends=(cmake pybind11)
optdepends=('gurobi: for ILP solver in ilp_improve')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('20be12754cae835fe76243f704e0e50c70620186c549de1b45a8a957e75317713925a0d00c9360fc5dd1e9f679f92f8d797ccf8d7005f7fbe740089890da7126')

build() {
  cmake \
    -S ${_base}-${pkgver} \
    -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_SHARED_LIBS=TRUE \
    -DCMAKE_CXX_STANDARD=11 \
    -DCMAKE_C_COMPILER=gcc \
    -DCMAKE_CXX_COMPILER=g++ \
    -DCMAKE_C_FLAGS="-O3 -DNDEBUG -fPIC" \
    -DCMAKE_CXX_FLAGS="-O3 -DNDEBUG -fPIC -fpermissive" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-as-needed" \
    -DCMAKE_VERBOSE_MAKEFILE=OFF \
    -DBUILDPYTHONMODULE=ON \
    -DUSE_TCMALLOC=OFF \
    -DUSE_ILP=OFF \
    -D64BITMODE=OFF \
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

# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.21
pkgrel=2
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=(x86_64)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmpi python)
makedepends=(cmake pybind11) # python-build python-installer python-scikit-build-core python-setuptools-scm
optdepends=('gurobi: for ILP solver in ilp_improve')
options=(!emptydirs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('3a29be7d4131d8c61cdf9cee1ad3cfbdfb06cbdbd8d60965269735e577991a71b6c08784245384d2884ba46ac9b7125dc47eb2d934ab5c2e32c031143ade9bfa')

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
  # cd ${_base}-${pkgver}
  # export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  # python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  DESTDIR="${pkgdir}" cmake --build build --target install
  # cd ${_base}-${pkgver}
  # PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  local _pyversion=$(python -c "import sys; print(f'{sys.version_info.major}{sys.version_info.minor}')")
  install -dm755 "${pkgdir}${site_packages}/${_base,,}"
  mv "build/${_base,,}.cpython-${_pyversion}-${CARCH}-linux-gnu.so" "${pkgdir}${site_packages}/${_base,,}"
  install -Dm 644 ${_base}-${pkgver}/python/${_base,,}/__init__.py -t "${pkgdir}${site_packages}/${_base,,}"
  install -Dm 644 ${_base}-${pkgver}/LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -r "${pkgdir}/${_base,,}"
}

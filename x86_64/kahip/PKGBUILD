# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Mohamed Amine Zghal (medaminezghal) <medaminezghal at outlook dot com>
_base=KaHIP
pkgname=${_base,,}
pkgver=3.22
pkgrel=1
pkgdesc="Karlsruhe HIGH Quality Partitioning"
arch=(x86_64)
url="https://github.com/${_base}/${_base}"
license=(MIT)
depends=(openmpi python)
makedepends=(cmake pybind11) # python-build python-installer python-scikit-build-core python-setuptools-scm
optdepends=('gurobi: for ILP solver in ilp_improve')
options=(!emptydirs)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b61fc043f81233dc5e6f1d2db2b955a8e801c8da6a0bb5c6adf250b59061cdba7fde53059a830dd8da33a88a289759835033ef3fb5340b2007032f566bca8e18')

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

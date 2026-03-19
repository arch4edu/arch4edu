pkgname=lief
pkgver=0.17.6
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=('x86_64')
url='https://github.com/lief-project/lief'
license=(Apache-2.0)
depends=(
  mbedtls
  libgcc
  libstdc++
  glibc
)
optdepends=(
  'python: python bindings'
)
conflicts=(
  python-lief
)
makedepends=(
  cmake
  python
  nlohmann-json
  python-build
  python-installer
  python-wheel
  python-tomli
  python-scikit-build-core
  ninja
  python-cattrs
  python-packaging
  python-rich
  python-setuptools
  python-pydantic
  python-pydantic-core
  python-pyproject-metadata
  python-pathspec
  tl-expected
)
#checkdepends=(
#  python-pytest
#)
provides=(libLIEF.so)
source=(
	"lief-${pkgver}.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz"
)
b2sums=('5f06b8c35e245cf7a5fc1a394f30e060a939469120c2525bf83c7d9180cc165d11b08a43d5e0a71f7959adeabff4c7d76e52e80fe9ea47360598ff37a1729fad')

prepare() {
  cd "LIEF-$pkgver"
  # unpin versions
  sed 's/==.*//' --in-place api/python/build-requirements.txt
}

build() {
  local cmake_options=(
    -B build_dir
    -S LIEF-$pkgver
    -G "Ninja"
    -D CMAKE_BUILD_TYPE=Release
    -D BUILD_SHARED_LIBS=ON
    -D LIEF_EXAMPLES=OFF
    -D LIEF_PYTHON_API=ON
    -D LIEF_OPT_NLOHMANN_JSON_EXTERNAL=ON
    -D LIEF_OPT_MBEDTLS_EXTERNAL=ON
    -D LIEF_OPT_EXTERNAL_EXPECTED=ON
    -D LIEF_RUST_API=ON
    -D LIEF_DEX=ON
    -D LIEF_PE=ON
    -D LIEF_TESTS=OFF
  )
  cmake "${cmake_options[@]}"
  cmake --build build_dir

  cd "LIEF-$pkgver"
  python -m build --wheel --no-isolation api/python
}

#check() {
#  ctest --output-on-failure --test-dir build_dir
#
#  python -m venv --without-pip --system-site-packages --clear venv
#  source venv/bin/activate
#  export LIEF_SAMPLES_DIR="${srcdir}/samples"
#  mkdir "${LIEF_SAMPLES_DIR}"
#
#  cd "LIEF-$pkgver"
#  python -m installer api/python/dist/*.whl
#  python tests/dl_samples.py
#  python tests/run_pytest.py
#  #python tests/run_tools_check.py
#  deactivate
#}

package() {
  DESTDIR="$pkgdir" cmake --install build_dir

  cd "LIEF-$pkgver"
  python -m installer --destdir="$pkgdir" api/python/dist/*.whl
}

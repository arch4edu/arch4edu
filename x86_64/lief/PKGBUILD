# Maintainer: Xeonacid <h.dwwwwww dot gmail.com>
# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.16.5
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=('x86_64')
url='https://github.com/lief-project/lief'
license=(Apache-2.0)
depends=(
  mbedtls
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
provides=(libLIEF.so)
source=(
	"lief-${pkgver}.tar.gz::$url/archive/refs/tags/$pkgver.tar.gz"
	fix-missing-headers.patch
)
sha256sums=('10ef46bc958d7936feb155040c874504ab0bd40dc59b4678f807691ccd0d138f'
            'eea63ef3250abcda3a684925c5db6bcd592e52f3af75ef97d488bcb7b5735a6e')

prepare() {
  cd "LIEF-$pkgver"
  cat ../fix-missing-headers.patch | patch -p1
  sed 's/==.*//' --in-place api/python/build-requirements.txt
}

build() {
  cd "LIEF-$pkgver"
  cmake \
    -B build \
    -G "Ninja" \
    -D CMAKE_BUILD_TYPE=Release \
    -D BUILD_SHARED_LIBS=ON \
    -D LIEF_EXAMPLES=OFF \
    -D LIEF_PYTHON_API=ON \
    -D LIEF_OPT_NLOHMANN_JSON_EXTERNAL=ON \
    -D LIEF_OPT_MBEDTLS_EXTERNAL=ON \
    -D LIEF_OPT_EXTERNAL_EXPECTED=ON \
    -D LIEF_RUST_API=ON \
    -D LIEF_DEX=ON \
    -D LIEF_DOC=OFF \
    -D LIEF_PE=ON \
    -D LIEF_TESTS=OFF
  cmake --build build

  python -m build --wheel --no-isolation api/python
}

check() {
  cd "LIEF-$pkgver"
  #ctest --output-on-failure --test-dir build
  #python tests/run_pytest.py
  #python tests/run_tools_check.py
}

package() {
  cd "LIEF-$pkgver"
  DESTDIR="$pkgdir" cmake --install build

  python -m installer --destdir="$pkgdir" api/python/dist/*.whl
}

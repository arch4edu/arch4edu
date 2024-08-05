# Maintainer: Xeonacid <h.dwwwwww dot gmail.com>
# Maintainer: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgbase=lief
pkgname=(lief python-lief)
pkgver=0.15.1
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=('x86_64')
url='https://github.com/lief-project/lief'
license=(Apache-2.0)
depends=(tl-expected)
makedepends=(cmake python nlohmann-json python-build python-installer python-wheel python-tomli python-scikit-build-core ninja python-cattrs python-packaging python-rich python-setuptools python-pydantic python-pydantic-core python-pyproject-metadata python-pathspec)
provides=(libLIEF.so)
source=($url/archive/refs/tags/$pkgver.tar.gz)
sha256sums=('28653b59afc8b8b255251f21a0f3cbfbdec05dd988fb3f473e22dde28f427ad8')

prepare() {
  cd "LIEF-$pkgver/api/python"
  sed -i 's/==.*//' build-requirements.txt
}

build() {
  cd "LIEF-$pkgver"
  cmake \
    -B build \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DLIEF_EXAMPLES=OFF \
    -DLIEF_PYTHON_API=ON \
    -DLIEF_OPT_NLOHMANN_JSON_EXTERNAL=ON \
    -DLIEF_OPT_EXTERNAL_EXPECTED=ON
  cmake --build build

  cd api/python
  python -m build --wheel --no-isolation
}

package_lief() {
  cd "LIEF-$pkgver"
  DESTDIR="$pkgdir" cmake --install build
}

package_python-lief() {
  depends+=(python lief)
  cd "LIEF-$pkgver/api/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}

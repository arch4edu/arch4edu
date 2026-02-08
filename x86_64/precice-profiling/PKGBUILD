# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=profiling
pkgname=precice-${_base}
pkgdesc="A tool for post-processing and analyzing preCICE profiling data"
pkgver=2.1.0
pkgrel=2
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-typing_extensions python-orjson python-polars python-matplotlib perfetto)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('2485f62fa9f2fa9c1c4c5c06b2df0fdd79f713f71ab9cdab7a7b09b96967da01cb5d3f2de92126fe81ff3e0c65bb8e5073266187161c0cbb2ba42843899442b9')

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest tests
}

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

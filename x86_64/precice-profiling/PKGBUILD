# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=profiling
pkgname=precice-${_base}
pkgdesc="A tool for post-processing and analyzing preCICE profiling data"
pkgver=2.0.1
pkgrel=2
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-typing_extensions python-orjson python-polars python-matplotlib graphviz)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('b022a15a36fab46975774f4135f78e1de9838fb0dd70d94008af62c8c28ae81249d66eaea83b20d034a8e8fb34e78a73a0bd06f4294fd6972fe921af1a4df9b7')

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

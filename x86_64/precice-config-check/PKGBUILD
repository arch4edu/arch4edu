# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-check
pkgname=precice-${_base}
pkgdesc="Python tool that checks a preCICE configuration file for logical errors"
pkgver=1.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(precice-config-graph)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('1f504367cf071c917efe89580c48df541e2f6f25a0c12954096c5d2634e2d8831a1ba059f28e16b00b8b1386dd264f5ac2c4a54edf71f60bc066c420af84d3ed')

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

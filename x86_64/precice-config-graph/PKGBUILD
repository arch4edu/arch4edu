# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-graph
pkgname=precice-${_base}
pkgdesc="A Library that builds a graph from a preCICE configuration file for validation and visualization purposes"
pkgver=3.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-networkx precice-config-format)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest python-gitpython)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('271de157a11e170945128c739143b676680974538fdc00903b3f093d08c8cd561952ea72dde3b2bec4925b19b7ae57c24e8cb868416a098d707fdf5c6a0a8ab7')

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

# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-graph
pkgname=precice-${_base}
pkgdesc="A Library that builds a graph from a preCICE configuration file for validation and visualization purposes"
pkgver=2.0.1
pkgrel=2
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-elementpath python-matplotlib python-networkx)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest python-gitpython)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('ae6d7e68f9d228d8352250bd2b8c880565de44a7989bcda4ce9098df52cd853cf95a70f40fb61ea03a7b368d79bbf769da355aa3f0c99b09b64c81ad47ddd4b2')

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

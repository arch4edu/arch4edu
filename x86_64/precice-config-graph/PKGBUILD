# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-graph
pkgname=precice-${_base}
pkgdesc="A Library that builds a graph from a preCICE configuration file for validation and visualization purposes"
pkgver=2.0.2
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-elementpath python-matplotlib python-networkx)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest python-gitpython)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('1c4e31a66e30c63017391065c44c98a13d74253aa4976cae641ef8cf816bd983c74189aa01dfb23a63db0ced6952d418b264b923b4257c723bdac9b63f1bc83b')

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

# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-graph
pkgname=precice-${_base}
pkgdesc="A Library that builds a graph from a preCICE configuration file for validation and visualization purposes"
pkgver=1.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-elementpath python-matplotlib python-networkx)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('f44e656e71b7b5e6c60205f1df4734c5a35f2ff87128cb7b004bf61fecb6dc6952de18827a0f4eb0fbf9470b741b349c2c73890e39709b8875a4171921a7f660')

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

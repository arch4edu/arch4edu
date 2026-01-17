# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-graph
pkgname=precice-${_base}
pkgdesc="A Library that builds a graph from a preCICE configuration file for validation and visualization purposes"
pkgver=2.0.5
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-elementpath python-matplotlib python-networkx)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest python-gitpython)
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('a29969f7aeeb420a911b536c97336f1e79922ec554e7cd677eab2ac7bf3e8c4e6173886a9b309ddb22b109ff9f97e939dd1ea064c1012247aed98a3a96e731f6')

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

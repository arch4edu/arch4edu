# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=config-visualizer
pkgname=precice-${_base}
pkgdesc="A tool for visualizing a preCICE configuration file as a dot file"
pkgver=2.0.0
pkgrel=1
arch=(any)
url="https://github.com/precice/${_base}"
license=(MIT)
depends=(python-lxml python-pydot python-typing_extensions)
makedepends=(python-build python-installer python-setuptools-git-versioning git)
checkdepends=(python-pytest)
optdepends=('precice-config-visualizer-gui: for gui support')
source=(git+${url}.git#tag=v${pkgver})
sha512sums=('34dfc2327297fa9f567729c1260a2c35022f3306ff4e60e966b0d3c1d690e9bc5a094889e1d9bf14903bd86e0406124762b35b1c49d2e5fb892bced14b9e5ff9')

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
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 README.md -t "${pkgdir}/usr/share/doc/${pkgname}"
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

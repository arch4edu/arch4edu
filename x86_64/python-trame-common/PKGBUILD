# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-common
pkgname=python-${_base}
pkgdesc="Dependency less classes and functions for trame"
pkgver=1.0.0
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python)
makedepends=(python-build python-installer python-hatchling)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('7e46d343e959387d9f8746be5907cf55d89704539df4a6d7b38a250f0e73e49b9b0755eb9d44ae849d0ad7fac0f0e3e1ecb0ad603e4f8b144723381581684bb6')

build() {
  cd ${srcdir}/${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

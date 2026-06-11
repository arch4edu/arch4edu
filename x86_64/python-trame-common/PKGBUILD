# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-common
pkgname=python-${_base}
pkgdesc="Dependency less classes and functions for trame"
pkgver=1.2.3
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python)
makedepends=(python-build python-installer python-hatchling)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('c8ddb8fb955b65aa5db6d5ea46f6df4e87ef8912a3412ed0407509baa2beaa15627e616da7aebf927f364dfc0c39f3431f34ff2569d920e1df7feef1e838ae92')

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

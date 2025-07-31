# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-common
pkgname=python-${_base}
pkgdesc="Dependency less classes and functions for trame"
pkgver=1.0.1
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(Apache-2.0)
depends=(python)
makedepends=(python-build python-installer python-hatchling)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('24738e0ff85d172e877036c6fbec951056af5830b72a357b6aabb597fbf934f73cf6da6b12cb5c3ec9ee0f13009d1fbbf1c0b4a32b70e7c355bf49a6c3ad5c8d')

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

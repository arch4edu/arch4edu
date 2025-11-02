# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ufl
pkgname=python-fenics-${_base}
pkgdesc="UFL - Unified Form Language"
pkgver=2025.2.0.post0
pkgrel=1
arch=(any)
url="https://github.com/FEniCS/${_base}"
license=(LGPL-3.0-or-later GPL-3.0-or-later)
depends=(python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('adc6b0a42cf7721c3641a8a1dbb82643b53119e3cdde1d24ad3fccb741e3f1604881dfc9196258f9ecd1ef3f8a8e98ae9dcc6d8b3b6b5dce27195eaf7a59f10c')
provides=("python-${_base}")
conflicts=("python-${_base}" "python-${_base}-git")

build() {
  cd ${_base}-${pkgver}
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
  install -Dm 644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

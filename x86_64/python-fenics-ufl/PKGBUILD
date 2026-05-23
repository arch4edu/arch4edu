# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ufl
pkgname=python-fenics-${_base}
pkgdesc="UFL - Unified Form Language"
pkgver=2025.3.0
pkgrel=1
arch=(any)
url="https://github.com/FEniCS/${_base}"
license=(LGPL-3.0-or-later GPL-3.0-or-later)
depends=(python-numpy)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('5665a437694deac1f7434ebb06c533df89bb5a98d0ad83e07a6f4855b10c24bc9e317d7c24be94a9585404142fb4d746b148796af55b226ff472945df8ca5484')
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

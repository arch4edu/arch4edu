# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=basix
pkgname=python-fenics-${_base}
pkgdesc="Basix Python interface"
pkgver=0.10.0.post0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(basix python-numpy)
makedepends=(python-build python-installer python-scikit-build-core python-wheel nanobind)
checkdepends=(python-pytest python-fenics-ufl python-matplotlib python-numba python-scipy python-sympy)
optdepends=('python-numba: for Numba helper function support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('74b4fd9717c058c5824748b3f7f6747f2ee5915ee0b83794b42cee542fab89fcdac3e0f66c1110cd90d21377ac97335dc696cd62e6882fc155ead762e43d02df')

build() {
  cd ${_base}-${pkgver}/python
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer python/dist/*.whl
  test-env/bin/python -m pytest test \
    --ignore test/test_dof_ordering.py
  test-env/bin/python demo/python/demo_*.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" python/dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

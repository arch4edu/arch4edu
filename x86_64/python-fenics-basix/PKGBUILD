# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=basix
pkgname=python-fenics-${_base}
pkgdesc="Basix Python interface"
pkgver=0.5.1
pkgrel=2
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
makedepends=(python-build python-installer python-scikit-build pybind11)
depends=(basix python-numpy)
checkdepends=(python-pytest python-sympy python-fenics-ufl) # python-numba python-scipy
optdepends=('python-numba: for Numba helper function support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('108acd1c6ab696e4dc15e3f8ae157285e9cd4b2e322837a504a036675320bc27cf411e69986015b304a5d8681db6f562beb2e7f1b5794bbe7a2e0eadd747ba0f')

build() {
  cd ${_base}-${pkgver}/python
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer python/dist/*.whl
  test-env/bin/python -m pytest -k 'not numba'
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" python/dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

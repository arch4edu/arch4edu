# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=basix
pkgname=python-fenics-${_base}
pkgdesc="Basix Python interface"
pkgver=0.10.0
pkgrel=2
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(basix python-numpy)
makedepends=(python-build python-installer python-scikit-build-core python-wheel nanobind)
checkdepends=(python-pytest python-fenics-ufl python-matplotlib python-numba python-scipy python-sympy)
optdepends=('python-numba: for Numba helper function support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('71bd73ec9335e918cd37d6369d8768f0639d43395cfcb3ee8d15fe956e8c92d077922fe4557187e97c004a2e2d2ca662748e771bcbd0e4cb4ef613059c399aae')

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

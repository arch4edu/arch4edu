# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=basix
pkgname=python-fenics-${_base}
pkgdesc="Basix Python interface"
pkgver=0.9.0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(basix python-numpy)
makedepends=(python-build python-installer python-scikit-build-core python-wheel nanobind)
checkdepends=(python-pytest python-fenics-ufl python-matplotlib python-numba python-scipy python-sympy)
optdepends=('python-numba: for Numba helper function support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('0ea49f7710265ef7d3d61607285c263b923265af8d1435ebeb557f26281bca593a1ee711c2c3f3bf97048cb5e226e574279f22fd2c6d3898e4f1e5b48251f806')

build() {
  cd ${_base}-${pkgver}/python
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer python/dist/*.whl
  test-env/bin/python -m pytest test \
    -k 'not permute_subentity_closure'
  test-env/bin/python demo/python/demo_*.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" python/dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

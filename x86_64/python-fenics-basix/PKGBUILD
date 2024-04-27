# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=basix
pkgname=python-fenics-${_base}
pkgdesc="Basix Python interface"
pkgver=0.8.0
pkgrel=2
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(basix python-numpy)
makedepends=(python-build python-installer python-scikit-build-core python-wheel nanobind)
checkdepends=(python-pytest python-sympy python-fenics-ufl) # python-numba
optdepends=('python-numba: for Numba helper function support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('4f259173e97da9141b79f66e76baddab9e0d00f672feedde18742ac95d6d31668b80e319b939a67a4558bc7dd8e7479d9c75f3a1c2bf5abdf077ed3202ea4f99')

prepare() {
  # https://github.com/FEniCS/basix/issues/811
  sed -i 's/^wheel.license-files/#wheel.license-files/' ${_base}-${pkgver}/python/pyproject.toml
  sed -i 's/^license/#license/' ${_base}-${pkgver}/python/pyproject.toml
}

build() {
  cd ${_base}-${pkgver}/python
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer python/dist/*.whl
  test-env/bin/python -m pytest --ignore=test/test_numba.py
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" python/dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

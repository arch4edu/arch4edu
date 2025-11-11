# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ffcx
pkgname=python-fenics-${_base}
pkgdesc="The FEniCSx Form Compiler"
pkgver=0.10.1
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(LGPL-3.0-or-later GPL-3.0-or-later Unlicense)
depends=(python-cffi python-fenics-basix python-fenics-ufl python-setuptools)
makedepends=(python-build python-installer python-wheel)
checkdepends=(python-pytest python-numba python-pygraphviz python-sympy)
optdepends=('python-numba: for Numba C signature for the UFCx support'
  'python-pygraphviz: utility to draw graph')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('5cf953f5fdfc235a1f6ab55124b39d708705159d182e2a15f997efb35ca6633d2155182b578e7ba190c65b0568d64ceda36960c47a55878f3d5093341544362e')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  PATH="${PWD}/test-env/bin:$PATH" test-env/bin/python -m pytest
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl

  # Symlink license file
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  install -d ${pkgdir}/usr/share/licenses/${pkgname}
  ln -s "${site_packages}/fenics_${_base}-${pkgver}.dist-info/LICENSE" \
    "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

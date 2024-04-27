# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ffcx
pkgname=python-fenics-${_base}
pkgdesc="The FEniCSx Form Compiler"
pkgver=0.8.0
pkgrel=1
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(LGPL-3.0-or-later GPL-3.0-or-later Unlicense)
depends=(python-cffi python-fenics-basix python-fenics-ufl)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest python-sympy python-pygraphviz)
optdepends=('python-pygraphviz: utility to draw graph'
  'python-numba: for Numba C signature for the UFCx support')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('becd7a07b7e83c3c7538ed277de97c3366397042a446df84a6a91aab497aa10a1fa0452282db00cfc5119fe222bdd3416aa1abfdd982d3f7ae83cea62b0cbc08')

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

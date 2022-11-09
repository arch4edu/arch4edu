# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=ffcx
pkgname=python-fenics-${_base}
pkgdesc="The FEniCSx Form Compiler"
pkgver=0.5.0.post0
pkgrel=2
arch=(x86_64)
url="https://github.com/FEniCS/${_base}"
license=(MIT)
depends=(python-setuptools python-fenics-ufl python-fenics-basix python-cffi)
makedepends=(python-build python-installer python-wheel)
checkdepends=(python-pytest python-sympy python-pygraphviz)
optdepends=('python-pygraphviz: utility to draw graph')
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('816da71315a7494ee97782d8c7d8df93d646a2f7b3e213d532b4dcdea179dc49248ac71d1ad7e6cf5d5d1010dc399c37c2eb22a773a86b6434a964b192d65072')

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

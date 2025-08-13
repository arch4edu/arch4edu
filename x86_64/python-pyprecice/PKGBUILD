# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyprecice
pkgname=python-${_base}
pkgdesc="Python language bindings for the preCICE coupling library"
pkgver=3.2.1
pkgrel=1
arch=(x86_64)
url="https://github.com/${_base/py/}/python-bindings"
license=(LGPL-3.0-or-later)
depends=(precice python-mpi4py)
makedepends=(python-build python-installer python-setuptools cython python-pkgconfig python-wheel)
source=(python-bindings-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f0af6346ccfe2a8f0309a0fd6403fea0a6d800ea69efc5ab120bc7119e8ea43154f4757fe5a3c99f590752d7afbe96eefb8875c759943211b244376bc2cc48b5')

build() {
  cd python-bindings-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  # FIXME: https://github.com/precice/python-bindings/issues/1
  cd python-bindings-${pkgver}/examples/solverdummy
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer ../../dist/*.whl
  mpiexec -n 1 test-env/bin/python solverdummy.py precice-config.xml SolverOne &
  mpiexec -n 1 test-env/bin/python solverdummy.py precice-config.xml SolverTwo
}
package() {
  cd python-bindings-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}"/usr/share/licenses/"${pkgname}"
}

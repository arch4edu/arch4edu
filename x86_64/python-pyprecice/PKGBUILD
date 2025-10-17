# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyprecice
pkgname=python-${_base}
pkgdesc="Python language bindings for the preCICE coupling library"
pkgver=3.3.1
pkgrel=1
arch=(x86_64)
url="https://github.com/${_base/py/}/python-bindings"
license=(LGPL-3.0-or-later)
depends=(precice python-mpi4py)
makedepends=(python-build python-installer cython python-pkgconfig python-setuptools-git-versioning python-wheel git)
source=("git+${url}.git#tag=v${pkgver}")
sha512sums=('470aae9420c39e5f9733858f04b94ba824da16886e9b74c9d694c9e77ffe910b2cd0287a2563eb89ffaf586c9a5ae66ea0d10213618162f6ea1645a127959fdd')

build() {
  cd python-bindings
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  # FIXME: https://github.com/precice/python-bindings/issues/1
  cd python-bindings/examples/solverdummy
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer ../../dist/*.whl
  mpiexec -n 1 test-env/bin/python solverdummy.py precice-config.xml SolverOne &
  mpiexec -n 1 test-env/bin/python solverdummy.py precice-config.xml SolverTwo
}
package() {
  cd python-bindings
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE.txt -t "${pkgdir}"/usr/share/licenses/"${pkgname}"
}

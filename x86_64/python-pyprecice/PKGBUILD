# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=pyprecice
pkgname=python-${_base}
pkgdesc="Python language bindings for the preCICE coupling library"
pkgver=3.4.0
pkgrel=1
arch=(x86_64)
url="https://github.com/${_base/py/}/python-bindings"
license=(LGPL-3.0-or-later)
depends=(precice python-mpi4py)
makedepends=(python-build python-installer cython python-pkgconfig python-setuptools-git-versioning python-wheel git)
source=("git+${url}.git#tag=v${pkgver}")
sha512sums=('2d9782a42af294f537caa3a94b0f9b86f06133bd9ddb54b8443724a02388d79e66280e685455208f8f0fee7d11ae56d80a8d613133dd345fdece5742ef3f6e5f')

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

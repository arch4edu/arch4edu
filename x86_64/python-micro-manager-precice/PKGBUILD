# Maintainer: Gerasimos Chourdakis <chourdak at in dot tum dot de>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=micro-manager
pkgname=python-${_base}-precice
pkgdesc="A tool which facilitates two-scale macro-micro coupled simulations using preCICE"
pkgver=0.7.0
pkgrel=1
arch=(any)
url="https://precice.org/tooling-${_base}-overview.html"
license=(LGPL-3.0-or-later)
depends=(python-pyprecice python-psutil)
makedepends=(python-build python-installer python-setuptools python-setuptools-git-versioning python-wheel git)
checkdepends=(python-scikit-learn python-h5py-openmpi pybind11)
optdepends=('python-h5py: for snapshot computations'
  'python-scikit-learn: for crash handling by interpolation')
source=(git+https://github.com/precice/${_base}.git#tag=v${pkgver})
sha512sums=('cd727d32cbd072a9bbe0f5b9ee8998e9b7626463af643a51dac3b3322fdec914c0977d68896721a65fa0a4434036b23e1c21065e1f0b2a3fb19d3322418c6439')

prepare() {
  sed -i 's/GPL/LGPL/' ${_base}/pyproject.toml
  sed -i 's/GNU/GNU Lesser/' ${_base}/pyproject.toml
}

build() {
  cd ${_base}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/${_base/-/_}_precice-${pkgver}*.whl

  cd ${srcdir}/${_base}/tests/integration/test_unit_cube
  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-config-local-adaptivity.json &
  ${srcdir}/${_base}/test-env/bin/python unit_cube.py 2

  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-config-global-adaptivity.json &
  ${srcdir}/${_base}/test-env/bin/python unit_cube.py 2

  cd ${srcdir}/${_base}/tests/unit
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_micro_manager.py
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_interpolation.py
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_micro_simulation_crash_handling.py
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_hdf5_functionality.py
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_snapshot_computation.py

  ${srcdir}/${_base}/test-env/bin/python -m unittest test_domain_decomposition.py
  ${srcdir}/${_base}/test-env/bin/python -m unittest test_adaptivity_serial.py

  cd ${srcdir}/${_base}/examples
  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-python-config.json &
  ${srcdir}/${_base}/test-env/bin/python macro_dummy.py no_adaptivity

  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-python-adaptivity-config.json &
  ${srcdir}/${_base}/test-env/bin/python macro_dummy.py adaptivity

  pushd cpp-dummy
  c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) micro_cpp_dummy.cpp -o micro_dummy$(python3-config --extension-suffix)
  popd

  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-cpp-config.json &
  ${srcdir}/${_base}/test-env/bin/python macro_dummy.py no_adaptivity

  ${srcdir}/${_base}/test-env/bin/micro-manager-precice micro-manager-cpp-adaptivity-config.json &
  ${srcdir}/${_base}/test-env/bin/python macro_dummy.py adaptivity
}

package() {
  cd ${_base}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"
}

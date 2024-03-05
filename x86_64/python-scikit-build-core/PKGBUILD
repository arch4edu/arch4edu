# Maintainer: Blair Bonnett <blair.bonnett@gmail.com>

pkgname=python-scikit-build-core
pkgdesc='Next generation Python CMake adaptor and Python API for plugins'
url='https://scikit-build-core.readthedocs.io/'
pkgver=0.8.1
pkgrel=1
arch=('any')
license=('Apache-2.0')

depends=(
  'cmake'
  'ninja'
  'python-cattrs'
  'python-packaging'
  'python-pathspec'
  'python-pyproject-metadata'
  'python-rich'
)
makedepends=('python-build' 'python-hatchling' 'python-hatch-vcs' 'python-installer')
checkdepends=(
  'cython'
  'gcc-fortran'
  'git'
  'pybind11'
  'python-hatch-fancy-pypi-readme'
  'python-numpy'
  'python-pip'
  'python-pytest'
  'python-pytest-subprocess'
  'python-setuptools-scm'
  'python-virtualenv'
)

_pypi=scikit_build_core
source=(
  "https://files.pythonhosted.org/packages/source/${_pypi::1}/$_pypi/$_pypi-$pkgver.tar.gz"
)
sha256sums=(
  'da058cff222e7fc0396bba7eae42af2ca35a684b7681ec4e9c91b1783b132030'
)

build() {
  cd "$_pypi-$pkgver"
  python -m build --wheel --no-isolation
}

check() {
  cd "$_pypi-$pkgver"
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer "dist/$_pypi-$pkgver"-*.whl
  test-env/bin/python -m pytest -v -k "not pep518_sdist and not test_setuptools_abi3"

  local _examples=(abi3 c cython fortran pybind11)
  for _example in "${_examples[@]}"; do
    echo ""
    echo "Building example docs/examples/getting_started/$_example"
    cd "$srcdir/$_pypi-$pkgver/docs/examples/getting_started/$_example"
    "$srcdir/$_pypi-$pkgver"/test-env/bin/python -m build --no-isolation --wheel

    echo "Testing example docs/examples/getting_started/$_example"
    "$srcdir/$_pypi-$pkgver"/test-env/bin/python -m installer dist/example-*.whl
    "$srcdir/$_pypi-$pkgver"/test-env/bin/python ../test.py
    "$srcdir/$_pypi-$pkgver"/test-env/bin/pip uninstall -yq example
  done
}

package() {
  cd "$_pypi-$pkgver"
  python -m installer --destdir="$pkgdir" "dist/$_pypi-$pkgver"-*.whl
}

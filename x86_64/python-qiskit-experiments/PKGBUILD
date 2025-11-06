# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-$_pkgname
pkgver=0.13.0
pkgrel=1
pkgdesc="Qiskit Experiments package for IBM qiskit framework"
arch=(any)
url=https://github.com/Qiskit-Community/qiskit-experiments
license=(Apache-2.0)
depends=(
    python-lmfit
    python-matplotlib
    python-numpy
    python-packaging
    python-pandas
    python-qiskit
    python-qiskit-ibm-experiment
    python-qiskit-ibm-runtime
    python-rustworkx
    python-scipy
    python-uncertainties
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
    python-wheel
)
optdepends=(
    'python-cvxpy: for tomography'
    'python-scikit-learn: for discriminators'
    'python-qiskit-aer: for simulating backends'
    'python-qiskit-dynamics: for the PulseBackend'
)
checkdepends=(
    python-cvxpy
    python-ddt
    python-fixtures
    python-multimethod
    python-pytest
    python-qiskit-aer
    python-scikit-learn
    python-testtools
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit-Community/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('b9159c23e987fb7096ed0d363e1961d013335a20e92b22c4173850687f126d7aed5c06a80ef5459557a7bc2445eec634023275bc57343156a50562672eb33edd')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
   cd $_pkgname-$pkgver
   local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
   python -m installer --destdir=../test_dir dist/*.whl
   PYTHONPATH="$PWD/../test_dir/$_site_packages" pytest
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-$_pkgname
pkgver=0.11.0
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
b2sums=('2ce8c8636afc832516bb5a53d08f46195e04d8c6d139c1c16ca572199c36f69ecb2ee9f1e0fa1afd931ad7dfa8ec2ee534b7ea68457708e82f7b251c9d5acbb7')

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

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-$_pkgname
pkgver=0.8.0
pkgrel=2
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
    python-rustworkx
    python-scipy
    python-uncertainties
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
optdepends=(
    'python-cvxpy: for tomography'
    'python-scikit-learn: for discriminators'
    'python-qiskit-aer'
    'python-qiskit-dynamics: for the PulseBackend'
)
#checkdepends=(
#    python-ddt
#    python-fixtures
#    python-multimethod
#    python-pytest
#    python-qiskit-aer
#    python-testtools
#)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit-Community/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('aa249eda1e8ab8798ef9e883d5929e11810fe7e22f72a1a19c5f20202ffe2a557dd986b2fba6b37bb897bfe3ab3e08bd0f35e28d6dd6899b7b62f5cd8065f615')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

#check() {
#    cd $_pkgname-$pkgver
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    python -m installer --destdir=../test_dir dist/*.whl
#    PYTHONPATH=../test_dir/$_site_packages pytest
#}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

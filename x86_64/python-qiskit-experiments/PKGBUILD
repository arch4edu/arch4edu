# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-$_pkgname
pkgver=0.7.0
pkgrel=1
pkgdesc="Qiskit Experiments package for IBM qiskit framework"
arch=(any)
url=https://github.com/Qiskit-Extensions/qiskit-experiments
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
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit-Extensions/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('5ff725064884dddce5280d75b701fd79e4bf0c7c06d4c87e0840fe5039865c5b124b111e4c20f79ba73139d34b8d937c1f153aa8b75b6f61a9e1e24a4d7a2614')

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

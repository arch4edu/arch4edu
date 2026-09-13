# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.9.1
pkgrel=1
pkgdesc="Quantum Machine Learning package for IBM qiskit framework"
arch=(x86_64)
url="https://github.com/qiskit-community/qiskit-machine-learning"
license=(Apache-2.0)
depends=(
    blas-openblas
    python-dill
    python-numpy
    python-qiskit
    python-scikit-learn
    python-scipy
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(
    python-ddt
    python-pytest
    python-qiskit-ibm-runtime
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('f877ddfdee8741ed6223c4d724187a6178687c2adc19ffdcf69e9dc4fbbd5f62d892bfe76a123bc109fb588c1f2d0c6b0a30d806271f816d92eb72208176f75c')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    test-env/bin/python -P -m pytest -o addopts="" -k "not test_p_bfgs" # due to upstream bug
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

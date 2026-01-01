# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.9.0
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
b2sums=('f08e5874b8e2d9f8c82e65474ad3ec1e12dd9f5e2b543c2f7066aa9131857622e94cd7b85e8c899447e02d67a45b394fd2338ecd54644bf8ca10244e004526c2')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    PYTHONPATH="$PWD/../test_dir/$_site_packages" pytest test -k "not test_start"
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

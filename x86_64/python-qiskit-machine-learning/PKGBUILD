# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.8.2
pkgrel=3
pkgdesc="Quantum Machine Learning package for IBM qiskit framework"
arch=(x86_64)
url="https://github.com/qiskit-community/qiskit-machine-learning"
license=(Apache-2.0)
depends=(
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
b2sums=('aaa39abcca0b621ebfc10734ff52df2a4ca48fbe97dca686cec2fc7b1a591e7ae785f8d3dfbcd9b35dc0457d125cda63ee7890a1435fbc17ae0def22489bc7b9')

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

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-nature
pkgname=python-${_pkgname}
pkgver=0.8
pkgrel=1
pkgdesc="Quantum Nature package for IBM qiskit framework"
arch=(x86_64)
url=https://github.com/qiskit-community/qiskit-nature
license=(Apache-2.0)
depends=(
    python-h5py
    python-numpy
    python-qiskit
    python-qiskit-algorithms
    python-rustworkx
    python-scipy
    python-sympy
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
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('50555125b2b6650955b192b33e941b9cba5bd9f2c7ccda3b68d088e094634c5464ac6cce447dcbf441ad77d731889e0b9e932a92e201051a6f4d5f5dc5a2a6d6')

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

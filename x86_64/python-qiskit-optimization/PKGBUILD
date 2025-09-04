# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-optimization
pkgname=python-$_pkgname
pkgver=0.7.0
pkgrel=3
pkgdesc="Quantum Optimization package for IBM qiskit framework"
arch=(any)
url=https://github.com/qiskit-community/qiskit-optimization
license=(Apache-2.0)
depends=(
    blas-openblas
    python-docplex
    python-networkx
    python-numpy
    python-qiskit
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
    python-qiskit-aer
)
source=(
    $_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/$pkgver.tar.gz
    fix-test.patch::https://github.com/qiskit-community/qiskit-optimization/pull/682.patch
)
b2sums=('4f1116820f1baf360769ce24faeaf5ec6b33d847cdecfea019866bf0ebf727fc6d4e55fd77d10887e20e86d894e549776a17d703d1fc5b06bc7c156de444cec7'
        'ddbb5c7138dfef28cf02642b2f4f0a3a0607d761f8a9503b9aedafc94c07562f089c819ad62cbb9813209f651b7a4396dca83a66ce4c7d4cd40e013881038e9c')

prepare() {
    # https://github.com/qiskit-community/qiskit-optimization/issues/681
    patch -Np1 -d $_pkgname-$pkgver < fix-test.patch
}

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    PYTHONPATH=../test_dir/$_site_packages pytest test
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

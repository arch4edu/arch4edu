# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-optimization
pkgname=python-$_pkgname
pkgver=0.7.0
pkgrel=1
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
source=($_pkgname-$pkgver.tar.gz::https://github.com/qiskit-community/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('4f1116820f1baf360769ce24faeaf5ec6b33d847cdecfea019866bf0ebf727fc6d4e55fd77d10887e20e86d894e549776a17d703d1fc5b06bc7c156de444cec7')

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    python -m installer --destdir=../test_dir dist/*.whl
    # See https://github.com/qiskit-community/qiskit-optimization/issues/681
    PYTHONPATH=../test_dir/$_site_packages pytest -k "not test_samples_and_raw_samples"
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

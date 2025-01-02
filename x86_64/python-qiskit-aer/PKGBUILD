# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.15.1
pkgrel=2
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=(x86_64)
url="https://github.com/Qiskit/qiskit-aer"
license=(Apache-2.0)
depends=(
    blas-openblas
    cython
    muparserx
    nlohmann-json
    python-numpy
    python-psutil
    python-qiskit
    python-scipy
)
optdepends=(
    'openmp: parallelization with OpenMP'
    'python-cvxpy: support convex optimization'
    'python-dask: parallel computing with task scheduling'
    'python-distributed: distributed task scheduler for Dask'
)
makedepends=(
    cmake
    gcc-fortran
    ninja
    pybind11
    python-build
    python-installer
    python-scikit-build
    python-setuptools
    spdlog
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('521329642f141fbb5d4bb045f42b53e1a116614328837999d73e28c54fd7e1b8aa64d72080b54950575c264bd14349227b395363cc92ce384f1b4951d414862b')

prepare() {
    cd $_pkgname-$pkgver
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml
}

build() {
    cd $_pkgname-$pkgver
    DISABLE_CONAN=ON python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

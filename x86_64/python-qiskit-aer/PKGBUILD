# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.14.1
pkgrel=1
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
b2sums=('2385da498044d047f52c024e3a72f8bac3f0a9ff904b726bb16c0f2476b43806943a3a7ce332b31130ca5df8b7c34b6986c0a9205475fcdca257f68e2e9dfc91')

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

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.15
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
b2sums=('3a72d5e1c97e54dd9090bbd072ca52c03bc90d53ec13bdb52b20112adebde6ef4e85a5d3761d5cc9fab7bc8d41651865e538eaad591dad266533441114ae1ddc')

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

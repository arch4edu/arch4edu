# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.16
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=(x86_64)
url="https://github.com/Qiskit/qiskit-aer"
license=(Apache-2.0)
depends=(
    blas-openblas
    cython
    muparserx
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
    nlohmann-json
    pybind11
    python-build
    python-installer
    python-scikit-build
    python-setuptools
    spdlog
)
# checkdepends=(
#     python-ddt
#     python-pytest
#     python-stestr
# )
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('ddbad1c1c8be51806c5de524327312f8c56fb46f686b3c61b2059770485ff0022fab45faae55f22f2ac37e4cd6e71fd2d2b9c27c945639dc785b6dbb3a33492f')

prepare() {
    cd $_pkgname-$pkgver
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml
}

build() {
    cd $_pkgname-$pkgver
    DISABLE_CONAN=ON python -m build --wheel --no-isolation
}

# check() {
#    cd $_pkgname-$pkgver
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    python -m installer --destdir=../test_dir dist/*.whl
#    rm -rf qiskit_aer
#    PYTHONPATH=../test_dir/$_site_packages stestr run --slowest
# }

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

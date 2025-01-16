# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.16.0.1
pkgver_nlohmann_json=3.10.2
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
    ipython
    ninja
    pybind11
    python-build
    python-installer
    python-scikit-build
    python-setuptools
    spdlog
)
# checkdepends=(
#     python-ddt
#     python-matplotlib
#     python-pytest
#     python-qiskit-qasm3-import
#     python-seaborn
#     python-stestr
# )
source=(
    $_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz
    nlohmann-json-$pkgver_nlohmann_json.tar.gz::https://github.com/nlohmann/json/archive/refs/tags/v$pkgver_nlohmann_json.tar.gz
)
b2sums=('e924988ff639672447974b8523717d2c4d8af8935abfc144111d7ee93a8bf18db0d76159b4e4407d7fc29d433d555d09c952c383443912b6345b38ad39be07b6'
        'e7da213fb75d528b1f5425822f5b598e882f232a67670aaae2d8f89c76e72ee23fa3344d1acfef2b0338a6a423d17b231b7e047ff064c984c2ec7783b721a22c')

prepare() {
    cd $_pkgname-$pkgver
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml
}

build() {
    # We cannot use the header-only library from [extra] because of this issue:
    # https://github.com/Qiskit/qiskit-aer/issues/1742
    local cmake_options=(
        -B build
        -D JSON_BuildTests=OFF
        -D CMAKE_BUILD_TYPE=None
        -D CMAKE_INSTALL_PREFIX=/usr
        -D CMAKE_INSTALL_LIBDIR=/usr
        -D JSON_MultipleHeaders=OFF
        -S json-$pkgver_nlohmann_json
        -W no-dev
    )
    cmake "${cmake_options[@]}"
    cmake --build build --verbose
    DESTDIR=tmp cmake --install build

    cd $_pkgname-$pkgver
    export DISABLE_CONAN=ON
    export CPATH="$srcdir/tmp/usr/include:$CPATH"
    export nlohmann_json_DIR="$srcdir"/tmp/usr/cmake/nlohmann_json
    python -m build --wheel --no-isolation
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

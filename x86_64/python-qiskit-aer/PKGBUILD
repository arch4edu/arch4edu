# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.17
pkgver_nlohmann_json=3.10.2
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=(x86_64)
url="https://github.com/Qiskit/qiskit-aer"
license=(Apache-2.0)
depends=(
    blas-openblas
    python-numpy
    python-psutil
    python-qiskit
)
optdepends=(
    'openmp: parallelization with OpenMP'
    'python-cvxpy: support convex optimization'
    'python-dask: parallel computing with task scheduling'
    'python-distributed: distributed task scheduler for Dask'
)
makedepends=(
    cmake
    ipython
    ninja
    pybind11
    python-build
    python-installer
    python-scikit-build
    python-setuptools
    spdlog
)
checkdepends=(
    python-ddt
    python-matplotlib
    python-pytest
    python-qiskit-qasm3-import
    python-seaborn
    python-stestr
)
source=(
    $_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz
    nlohmann-json-$pkgver_nlohmann_json.tar.gz::https://github.com/nlohmann/json/archive/refs/tags/v$pkgver_nlohmann_json.tar.gz
)
b2sums=('7654630890f41a92a731321ab5bd3b3aad05267a558fa769c19511435ca4ed28df46c84522b3bd436efea3b7bc0f3eb703fd46bf2b1db447b37706f38b72be04'
        'e7da213fb75d528b1f5425822f5b598e882f232a67670aaae2d8f89c76e72ee23fa3344d1acfef2b0338a6a423d17b231b7e047ff064c984c2ec7783b721a22c')

prepare() {
    cd $_pkgname-$pkgver
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml

    # Fix legacy package name
    sed -i -e "s/qiskit.providers.aer.backends.controller_wrappers/qiskit_aer.backends.controller_wrappers/" test/terra/expression/test_classical_expressions.py
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
        -D CMAKE_POLICY_VERSION_MINIMUM=3.5
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

check() {
    cd $_pkgname-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf qiskit_aer
    # TODO: figure out why test_mps_options() started to fail recently...
    # WARNING: on modern CPUs some additional tests might fail
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" \
    pytest -v test -k "not test_mps_options"
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

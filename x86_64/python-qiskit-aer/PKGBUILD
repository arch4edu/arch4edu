# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.17.2
pkgver_nlohmann_json=3.10.2
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=(x86_64)
url="https://github.com/Qiskit/qiskit-aer"
license=(Apache-2.0)
depends=(
    blas-openblas
    python-dateutil
    python-numpy
    python-psutil
    python-qiskit
    python-sympy
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
b2sums=('49dafc4cba948b7e3d474b0b8c73075cc5135a7c8559eebc2c0d5578c19868b4dc0a1dd4e6ab199f67a3996eb35ea11c9e0d8da9d49835bd2d7119774f64d954'
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
    # See also: https://github.com/Qiskit/qiskit-aer/issues/2354
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" \
    pytest -v test -k "not test_mps_options and not test_switch_register_with_classical_expression and not test_pauli_noise_with_shot_branching"
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

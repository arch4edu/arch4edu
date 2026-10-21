# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.18.0
pkgrel=2
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=(x86_64)
url="https://github.com/Qiskit/qiskit-aer"
license=(Apache-2.0)
depends=(
    openblas
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
    git
    ipython
    ninja
    nlohmann-json
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
    $_pkgname::git+https://github.com/Qiskit/$_pkgname.git#tag=$pkgver
    fix-test-pauli-noise-with-shot-branching.patch
    fix-test-mps-options.patch
)
b2sums=('b6649e5078a58e61ddb56954622ab615ec7ff0a8bab7896caec99021197452490bfce18a93d1407a74fafa97f748eb679a4df06d2e90353fee3b059ca2bcaa54'
'6d622f326380020e8810cc727b760093d9abdc76a9e857f258bd0bab4354b4ebb1c44889013f66b4ff7ac73362d8b4d898c36c12e99dae1799b7342a81494f4d'
'5696c4848440b432348b8c6d51ed29d4640a50aea5df14904c4f216a76e67722251bef7b27f630aed4d82bca7fd3869240be8b252478325e0d971e78d364137b')

prepare() {
    cd $_pkgname
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml

    # Fix legacy package name
    sed -i -e "s/qiskit.providers.aer.backends.controller_wrappers/qiskit_aer.backends.controller_wrappers/" test/terra/expression/test_classical_expressions.py

    # Fix TestRuntimeParameterization::test_pauli_noise_with_shot_branching
    patch -Np1 < ../fix-test-pauli-noise-with-shot-branching.patch

    # Fix TestOptions::test_mps_options
    patch -Np1 < ../fix-test-mps-options.patch
}

build() {
    cd $_pkgname
    export DISABLE_CONAN=ON
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -rf qiskit_aer
    test-env/bin/python -P -m pytest -o addopts="" -v test
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

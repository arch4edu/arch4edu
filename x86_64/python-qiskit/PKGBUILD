# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=2.0.0
pkgrel=1
epoch=1
pkgdesc="An open-source SDK for working with (IBM) quantum computers"
arch=(x86_64)
url=https://github.com/Qiskit/qiskit
license=(Apache-2.0)
conflicts=(python-qiskit-terra)
depends=(
    python-dateutil
    python-dill
    python-numpy
    python-rustworkx
    python-scipy
    python-stevedore
    python-symengine-0.13
    python-sympy
)
optdepends=(
    'ipython: interactivity'
    'python-constraint: support for handling CSPs (Constraint Solving Problems)'
    'python-cvxpy: convex optimization problems'
    'python-matplotlib: plotting support'
    'python-pillow: image support'
    "python-pydot: Graphviz's Dot support"
    'python-pylatexenc: LaTeX support emoji selector'
    'python-qiskit-aer: high performance simulator for quantum circuits'
    'python-qiskit-experiments: tools for building, running, and analysis of experiments on noisy quantum computers'
    'python-qiskit-finance: stock/securities problems, portfolio optimizations and finance experiments'
    'python-qiskit-machine-learning: sample datasets and quantum classification algorithms'
    'python-qiskit-nature: ground state energy computations, excited states and dipole moments of molecules'
    'python-qiskit-optimization: quantum optimization algorithms'
    'python-qiskit-qasm3-import: import OpenQASM 3 files'
    'python-scikit-learn: machine learning and data mining'
    'python-seaborn: statistical data visualization'
    'python-z3-solver: theorem prover'
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-setuptools-rust
    python-wheel
)
checkdepends=(
    ipython
    python-ddt
    python-stestr
)
source=(
    $_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz
    14174.patch::$url/pull/14174.patch
)
b2sums=('da36cfbaaef52fe3f8e03916de0fc12ffd7ef8c1ce264e3b4558563909ee44ee5a85a3a61b7def07ba38e2061e9e154a98dddf5d7f280bf6b70b793176a53a65'
        'a963945c2bdace5c32c6dea4387b4567e6dd543174cc1d20539accdec3997edee47eb1149107e3f73e66745e371ddc62d9293881a3b5da8a0ab3d3d1410059c3')

prepare() {
    # Fix https://github.com/Qiskit/qiskit/issues/14169
    patch -Np1 -d $_pkgname-$pkgver < 14174.patch
}

build() {
    cd $_pkgname-$pkgver
    export CARGO_TARGET_DIR=target
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname-$pkgver
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf qiskit
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" \
    stestr run -d test/python -E "test_equivalence_draw"
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

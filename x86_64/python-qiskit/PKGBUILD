# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=1.3.2
pkgrel=2
epoch=1
pkgdesc="An open-source SDK for working with (IBM) quantum computers"
arch=(x86_64)
url=https://github.com/Qiskit/qiskit
license=(Apache-2.0)
conflicts=(python-qiskit-terra)
depends=(
    cython
    python-dateutil
    python-dill
    python-numpy
    python-rustworkx
    python-scipy
    python-stevedore
    python-symengine
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
# checkdepends=(
#     ipython
#     python-anyio
#     python-ddt
#     python-hypothesis
#     python-pillow
#     python-pytest
#     #python-pytest-benchmark
#     python-pytest-mock
#     #python-pytest-xdist
# )
source=($_pkgname-$pkgver.tar.gz::https://github.com/Qiskit/$_pkgname/archive/$pkgver.tar.gz)
b2sums=('e2f191f3231f858ded9c389f952a2207bfea4680be13db6207e9870fb08f2015c483e3fd891a298eaa531635cb7d1027bc10952b0c471dff9b89ed524e6228a3')

build() {
    cd $_pkgname-$pkgver
    export CARGO_TARGET_DIR=target
    python -m build --wheel --no-isolation
}

# check() {
#     cd $_pkgname-$pkgver
#     local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
#     python -m installer --destdir=../test_dir dist/*.whl
#     rm -rf qiskit
#     PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" \
#     pytest test/python -W ignore::DeprecationWarning -W ignore::PendingDeprecationWarning
# }

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

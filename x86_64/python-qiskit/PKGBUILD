# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=1.0.0
pkgrel=1
epoch=1
pkgdesc="An open-source SDK for working with quantum computers at the level of extended quantum circuits, operators, and primitives"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit"
license=('Apache-2.0')
provides=('python-qiskit-terra')
conflicts=('python-qiskit-terra')
depends=(
    'cython'
    'python-dateutil'
    'python-dill'
    'python-numpy'
    'python-rustworkx'
    'python-scipy'
    'python-stevedore'
    'python-symengine'
    'python-sympy'
)
optdepends=(
    'ipython: interactivity'
    'python-constraint: support for handling CSPs (Constraint Solving Problems)'
    'python-cvxpy: convex optimization problems'
    'python-matplotlib: plotting support'
    'python-pillow: image support'
    "python-pydot: Graphviz's Dot support"
    "python-pylatexenc: LaTeX support'emoji selector"
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
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-setuptools-rust'
    'python-wheel'
)
#checkdepends=(
#    'python-anyio'
#    'python-ddt'
#    'python-hypothesis'
#    'python-pytest'
#    'python-pytest-benchmark'
#    'python-pytest-xdist'
#)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('3e5903ef439e27770b24efe8a5dd7adafdee28d894a77255cae8a76f43d09e847d4f8da0face242eebc8f479beef846c00527a6e285f588271f07e91f89871d2')

build() {
    cd "${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
#    cd "${_pkgname}-${pkgver}"
#    python -m installer --destdir=test_dir dist/*.whl
#    # Delete qiskit folder so that the installed package is loaded and not the src
#    rm -rf qiskit
#    PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-${python_version}" pytest -v -k 'not test_examples' test/python
#}

package() {
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

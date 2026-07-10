# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=2.5.0
pkgrel=1
epoch=1
pkgdesc="An open-source SDK for working with (IBM) quantum computers"
arch=(x86_64)
url=https://github.com/Qiskit/qiskit
license=(Apache-2.0)
conflicts=(python-qiskit-terra)
depends=(
    python-dill
    python-numpy
    python-rustworkx
    python-scipy
    python-stevedore
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
    cargo
    cbindgen
    cmake
    git
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
provides=(libqiskit.so)
source=(
    $_pkgname::git+https://github.com/Qiskit/$_pkgname#tag=$pkgver
    fix-c-build.patch::https://patch-diff.githubusercontent.com/raw/Qiskit/qiskit/pull/16556.patch
)
b2sums=('a4ddddc69e5f9d865f8c63bc8321ea0d6812cd035a2bccb55240adfa11c119cefdb768181a4096d5375b3e292d6ee1c2b1f14f6cedb6e60ac0666e0b040bfd23'
        'e8adb5acfcf2bad9a55b71f3c70440443309a2887157e636d0bdb28d1ec83a8d04c5a24bedab6500e6fc487fe20a09bb0d438ed5f86c1659d320e092b45ace03')

prepare() {
    # https://github.com/Qiskit/qiskit/issues/16555
    patch -Np1 -d $_pkgname < fix-c-build.patch
}

build() {
    cd $_pkgname
    # Python wheel package
    export CARGO_TARGET_DIR=target
    python -m build --wheel --no-isolation
    # C shared library
    make c
}

check() {
    cd $_pkgname
    # Python unit tests
    local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    python -m installer --destdir=../test_dir dist/*.whl
    rm -rf qiskit
    PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" \
    stestr run -d test/python -E "test_equivalence_draw"
    # Test C library
    make ctest
}

package() {
    cd $_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm755 dist/c/lib/libqiskit.so "$pkgdir"/usr/lib/libqiskit.so
    install -Dm644 dist/c/include/qiskit.h "$pkgdir"/usr/include/qiskit.h
    install -Dm644 dist/c/include/qiskit/attributes.h "$pkgdir"/usr/include/qiskit/attributes.h
    install -Dm644 dist/c/include/qiskit/complex.h "$pkgdir"/usr/include/qiskit/complex.h
    install -Dm644 dist/c/include/qiskit/funcs.h "$pkgdir"/usr/include/qiskit/funcs.h
    install -Dm644 dist/c/include/qiskit/funcs_py.h "$pkgdir"/usr/include/qiskit/funcs_py.h
    install -Dm644 dist/c/include/qiskit/types.h "$pkgdir"/usr/include/qiskit/types.h
    install -Dm644 dist/c/include/qiskit/version.h "$pkgdir"/usr/include/qiskit/version.h
    install -Dm644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

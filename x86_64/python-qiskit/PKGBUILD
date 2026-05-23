# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=2.4.1
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
source=($_pkgname::git+https://github.com/Qiskit/$_pkgname#tag=$pkgver)
b2sums=('dc921c50f0be9533d863a1217dd35bfab32879ba14a856985e916d5dbe56225df82096408161e0714861d4ced51b5ebbf73a9490e4a9d4f9cbe0069496d6bde1')

prepare() {
    cd $_pkgname
    sed -i 's/setuptools-rust==1.12.0/setuptools-rust>=1.12.0/' pyproject.toml
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

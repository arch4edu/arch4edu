# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=0.46.0
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
    'python-ply'
    'python-psutil'
    'python-rustworkx'
    'python-scipy'
    'python-stevedore'
    'python-symengine'
    'python-sympy'
)
optdepends=(
    'python-qiskit-aer: high performance simulator for quantum circuits'
    'python-qiskit-experiments: tools for building, running, and analysis of experiments on noisy quantum computers'
    'python-qiskit-finance: stock/securities problems, portfolio optimizations and finance experiments'
    'python-qiskit-machine-learning: sample datasets and quantum classification algorithms'
    'python-qiskit-nature: ground state energy computations, excited states and dipole moments of molecules'
    'python-qiskit-optimization: quantum optimization algorithms'
    'cplex: commercial solver for mathematical optimization problems'
    'python-constraint: support for handling CSPs (Constraint Solving Problems)'
    'python-docplex: IBM Decision Optimization CPLEX Modeling'
    'python-ipywidgets: IPython HTML widgets for Jupyter'
    'python-matplotlib: plotting support'
    'python-pillow: image support'
    "python-pydot: Graphviz's Dot support"
    'python-pygments: syntax highlighter'
    'python-pylatexenc: LaTeX support'
    'python-qiskit-qasm3-import: import OpenQASM 3 files'
    'python-qiskit-toqm: Time-Optimal Qubit Mapping (TOQM) transpiler support'
    'python-seaborn: statistical data visualization'
    'python-tweedledum: synthesizing and manipulating quantum circuits'
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
b2sums=('35bb88f5d43582145a72945b0633665fb962ab27bde35ec7e290823cef41ae93bb4e0155728186d3eb9dfdb419efe014c127fcef12b69d93d259cba83ed3e57f')

build() {
    cd "${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
#    cd "${_pkgname}-${pkgver}"
#    python -m installer --destdir=test_dir dist/*.whl
#    # Delete qiskit folder so that the installed package is loaded and not the src
#    rm -rf qiskit
#    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest -v -k 'not test_examples' test/python
#}

package() {
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

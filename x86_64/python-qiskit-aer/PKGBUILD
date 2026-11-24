# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-$_pkgname
pkgver=0.18.4
pkgrel=1
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
source=($_pkgname::git+https://github.com/Qiskit/$_pkgname.git#tag=$pkgver)
b2sums=('bcc2247cad81a97987946f1b925859903e3d627ea4aa54ea7d0ff27927008b98bdbd1686deedd4213d907062434395bfcd424344bbc135777163901c6a7850d2')

prepare() {
    cd $_pkgname
    sed -i -e '/conan/d' -e '/cmake/d' -e '/ninja/d' pyproject.toml

    # Fix legacy package name
    sed -i -e "s/qiskit.providers.aer.backends.controller_wrappers/qiskit_aer.backends.controller_wrappers/" test/terra/expression/test_classical_expressions.py
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

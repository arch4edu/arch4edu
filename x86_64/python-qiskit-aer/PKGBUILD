# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-${_pkgname}
pkgver=0.12.0
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-aer"
license=('Apache')
depends=(
    'cython'
    'muparserx'
    'nlohmann-json'
    'openblas-lapack'
    'python-numpy'
    'python-qiskit-terra'
    'python-scipy'
)
optdepends=(
    'openmp: parallelization with OpenMP'
    'python-cvxpy: support convex optimization'
    'python-dask: parallel computing with task scheduling'
    'python-distributed: distributed task scheduler for Dask'
)
makedepends=(
    'cmake'
    'gcc-fortran'
    'ninja'
    'pybind11'
    'python-build'
    'python-installer'
    'python-scikit-build'
    'python-setuptools'
    'python-wheel'
    'spdlog'
)
source=(
    "${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz"
    "fix.patch"
)
b2sums=('8d14012ffb0e12f32dc954dfa883bc43be6ac7aa4e01597d6abb11c22d7f39e9b419ab78db0c613d951555590498e1f0a5dbc7bb7047d2a8e71ae9a6216c79ab'
        '17720f9591855941c0378ae38008a873d6c3c2f7496b2dda58fd85a2b156fe2d6307cc198727a3aaf483a4d1e60f84c97f878728a847d2c34a36831c7a9d3837')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch --forward --input="${srcdir}/fix.patch"
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    DISABLE_CONAN=ON python -m build --wheel --no-isolation
    #python setup.py bdist_wheel
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

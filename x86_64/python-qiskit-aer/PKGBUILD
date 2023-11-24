# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-${_pkgname}
pkgver=0.13.1
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-aer"
license=('Apache')
depends=(
    'blas-openblas'
    'cython'
    'muparserx'
    'nlohmann-json'
    'python-numpy'
    'python-qiskit'
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
    'spdlog'
)
source=(
    "${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz"
    "fix.patch"
)
b2sums=('a49f992a80ef644f34cb570d6cf85e147b7c897004c248ec749c43a64c5b950fe9d7f178c53b79202f73186c03e5bc61f36be76b904e22aa6f82a79b1b255bcf'
        '5523350559706d94f6eeb169360759d32bfd1dec8384948bfb04823eec6440e03377860ae53dc6ba3e7a9a087f0429d9f9bb4a4c3d7c523e713f5e6b34c20dc9')

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch --forward --input="${srcdir}/fix.patch"
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    DISABLE_CONAN=ON python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

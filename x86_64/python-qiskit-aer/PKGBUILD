# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-${_pkgname}
pkgver=0.11.1
pkgrel=1
pkgdesc="A high performance simulator for quantum circuits that includes noise models"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-aer"
license=('Apache')
depends=(
    'cython'
    'muparserx'
    'nlohmann-json'
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
    'lapack'
    'ninja'
    'openblas-lapack'
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
b2sums=(
    '3795e1f71914bbc0074a2eac10a82a28f3171d50f292a13dcb705f62daa5fa332a1eabd52391c1b168a822ca6428feb79fe08bb7c93cfd2f7ee5b0d38fed012b'
    '4b7763d6b5802f3e1275d760e84b323b4e786c6376615a0cfb440a3fdb1f53ee9f03eea6ed6e23ba245d1f159ecf1b10287b8aac65db76804d4aefb56f55c58e'
)

prepare() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    patch --forward --strip=1 --input="${srcdir}/fix.patch"
}

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    DISABLE_CONAN=1 python -m build --wheel --no-isolation
    #python setup.py bdist_wheel
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl

    # This deletes all folders except /usr/lib/python3.10/site-packages/qiskit/
    # See https://github.com/Qiskit/qiskit-aer/issues/1457
    find "${pkgdir}/usr" -mindepth 1 -maxdepth 1 -not -name lib -exec rm -rf '{}' \;

    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

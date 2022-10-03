# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-aer
pkgname=python-${_pkgname}
pkgver=0.11.0
pkgrel=2
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
    'python-dask: parallel computing with task scheduling'
    'python-distributed: distributed task scheduler for Dask'
)
makedepends=(
    'cmake'
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
#checkdepends=(
#    'python-pytest'
#    'python-fixtures'
#    'python-ddt'
#)
source=(
    "${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz"
    "fix.patch"
)

b2sums=(
    '1d48de7ef363475a09d145299de7a5a44417ab810c8821fe6ac7462c3b70004f7fb1a2e85a508f1bc8cd08e989918dc92105ab97ee94ab924fa6d9d386508894'
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

# TODO
#check() {
#    cd "${srcdir}/${_pkgname}-${pkgver}"
#    python -m installer --destdir="$srcdir/test" dist/*.whl
#    export PYTHONPATH="$srcdir"/test/usr/lib/python3.10/site-packages
#    python -m pytest test
#}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl

    # This deletes all folders except /usr/lib/python3.10/site-packages/qiskit/
    # See https://github.com/Qiskit/qiskit-aer/issues/1457
    find "${pkgdir}/usr" -mindepth 1 -maxdepth 1 -not -name lib -exec rm -rf '{}' \;

    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

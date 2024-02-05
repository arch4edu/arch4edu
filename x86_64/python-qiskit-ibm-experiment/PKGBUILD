# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.6
pkgrel=1
pkgdesc="Service that allows accessing the IBM Quantum experiment database."
arch=('any')
url="https://github.com/Qiskit-Extensions/qiskit-ibm-experiment"
license=('Apache-2.0')
depends=(
    'python-pandas'
    'python-qiskit'
    'python-requests'
    'python-requests-ntlm'
    'python-urllib3'
    'python-yaml'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit-Extensions/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('1571c5de78b491b4d8526da64d3450f5c63b68e1c13a4b5e06562d2c20e2cdd2c56270bf0da8c6ab0c581fac0f9d68025bbaec228051e3edf82db45e3a31cadf')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

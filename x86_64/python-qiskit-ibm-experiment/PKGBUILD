# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.2
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
b2sums=('7e41557189fd5829a9622001ae3b089d5b529edcd3bae4b23249a2faeb0ff5a5bee8efff70fe8c3d8e656e0c0512d8dfc2e4cbe7f0081d80950c2eb19c72b2b3')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

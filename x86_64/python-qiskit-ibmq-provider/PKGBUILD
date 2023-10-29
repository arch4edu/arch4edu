# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibmq-provider
pkgname=python-${_pkgname}
pkgver=0.20.2
pkgrel=2
pkgdesc="(DEPRECATED) Module for accessing the quantum devices and simulators at IBMQ"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibmq-provider"
license=('Apache')
depends=(
    'python-dateutil'
    'python-numpy'
    'python-qiskit-terra'
    'python-requests'
    'python-requests-ntlm'
    'python-urllib3'
    'python-websocket-client'
    'python-websockets'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('56970acf5992ef6252119cb693ad1158ed71072767ebdeb33e7b5a7a3c5235bd2d3b89d146fda7a4d67b365c1abcb60f828fbae25b59a5e1b404800ac819d671')
install="${pkgname}.install"

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

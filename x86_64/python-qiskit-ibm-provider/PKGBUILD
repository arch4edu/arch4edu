# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-provider
pkgname=python-${_pkgname}
pkgver=0.6.1
pkgrel=1
pkgdesc="Qiskit Provider for accessing the IBM Quantum Services: Online Systems and Simulators"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-provider"
license=('Apache')
depends=(
    'python-dateutil'
    'python-numpy'
    'python-qiskit-terra'
    'python-requests'
    'python-requests-ntlm'
    'python-typing_extensions'
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('0b0e91b7547fc1583e9dd7e20b75f3acb80478433347f9ab03ca96a59e97b30811d37d25b840f6a9e63a50e40aa50a61c702944da6456ff4633bf270178d048e')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

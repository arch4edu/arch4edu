# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-provider
pkgname=python-${_pkgname}
pkgver=0.7.3
pkgrel=1
pkgdesc="Qiskit Provider for accessing the IBM Quantum Services: Online Systems and Simulators"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-provider"
license=('Apache')
depends=(
    'python-dateutil'
    'python-numpy'
    'python-qiskit'
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
b2sums=('36b225ba8be5824fc6ba3214acfba04ae97a441010b377350844103e3fb824663e35d9bb580b9baa3fa88f278c41c0c5da2c898e89a4e4ca5042b8851934ce67')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

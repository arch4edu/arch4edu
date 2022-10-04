# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.6.2
pkgrel=2
pkgdesc="IBM Client for Qiskit Runtime"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-runtime"
license=('Apache')
depends=(
    'python-dateutil'
    'python-ibm-platform-services'
    'python-numpy'
    'python-qiskit-terra'
    'python-requests'
    'python-requests-ntlm'
    'python-typing_extensions'
    'python-urllib3'
    'python-websocket-client'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('5ee1fc314895168dc2c982f25d257e0f1958bfeb287c068e7e31762398bd5aaf8fe7b86be25dd6f5c1567a7d6f1639a32a1309dbaca9b4496387c7c52b3b066b')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-runtime
pkgname=python-${_pkgname}
pkgver=0.11.2
pkgrel=1
pkgdesc="IBM Client for Qiskit Runtime"
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-runtime"
license=('Apache')
depends=(
    'python-dateutil'
    'python-ibm-platform-services'
    'python-numpy'
    'python-qiskit-ibm-provider'
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
b2sums=('3634b3c1067c09e9520805335693eb7dbd433ff2cbd675f411ad4c5455a77174ba772d19d91d4f0636ba9417671bdfc91886150ef3ffe30580b0b833f100f7ac')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

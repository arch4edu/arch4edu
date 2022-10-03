# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibmq-provider
pkgname=python-${_pkgname}
pkgver=0.19.2
pkgrel=1
pkgdesc="Module for accessing the quantum devices and simulators at IBMQ"
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
b2sums=('026ee74fffd6a1de02f90ea9d602de397f2aa8ca70abbe869f09d596a43c91d37b5a2ffce18879167258d0a4b0d5e129cd560ced2f63c5a684b51fce589417e6')
install="${pkgname}.install"

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

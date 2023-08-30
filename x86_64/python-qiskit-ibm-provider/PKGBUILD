# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-provider
pkgname=python-${_pkgname}
pkgver=0.7.0
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
b2sums=('05583cad0602cda6969e76e9ed7c92bda6ac4e55c862bc49a1e8de603041e9ecea8da9906cc8d58910e162124a609168ac9a7fa6f27a12274ffbf177dd84fdd0')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

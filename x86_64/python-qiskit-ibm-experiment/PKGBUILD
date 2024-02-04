# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.5
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
b2sums=('88fc38d2120f6a8936630815a15e13f1209b98f90dd0b6cfa970db8f3edb3c3e84bf489ae7317b28326e11b1f08346070e751c629769f3b5d2a9de278a0448be')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

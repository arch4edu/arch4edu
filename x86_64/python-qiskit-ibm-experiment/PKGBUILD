# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.4
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
b2sums=('ba541826004f64183671a334426c581f827092fafbe497f8932fe92c852ae39bff74f22efaff352786df9d8ff2aff7b34acd8f8d653badd913ceb19fcd9b6970')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

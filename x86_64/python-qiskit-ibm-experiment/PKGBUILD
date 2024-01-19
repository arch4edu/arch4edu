# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.4.1
pkgrel=1
pkgdesc="Service that allows accessing the IBM Quantum experiment database."
arch=('any')
url="https://github.com/Qiskit-Extensions/qiskit-ibm-experiment"
license=('Apache')
depends=(
    'python-pandas'
    'python-qiskit'
    'python-requests-ntlm'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit-Extensions/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('f693085c86e39aa9d7b54a56bdce0f7b7fef8c6fb2368721e7e5fa69dd9c1f5e05e774f6c8f67f92bfc9c68234ca09353374e51f898980241f7cd2bdb1458ef8')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

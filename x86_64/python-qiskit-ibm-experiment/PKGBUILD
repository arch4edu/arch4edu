# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.3.4
pkgrel=1
pkgdesc="Service that allows accessing the IBM Quantum experiment database."
arch=('any')
url="https://github.com/Qiskit/qiskit-ibm-experiment"
license=('Apache')
depends=(
    'python-pandas'
    'python-qiskit-terra'
    'python-requests-ntlm'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('1f72c7169a4617fc9c238f0902c555a65b80098339780aad3cfeb6345447c5f3e271da4d242dc97b805b343226561bb6ed3881a6b453a6d4653a166b3443f9b3')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

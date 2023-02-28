# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-ibm-experiment
pkgname=python-${_pkgname}
pkgver=0.2.8
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
b2sums=('fb1a1c86f4a744e7e874dea9146c34c8f983321001c2d62ad4ffd1a42a376cb03fc1573f1f3d7d2f3e0ac4ddda103faa13de43538626f68ead0c1e12d50dd240')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-${_pkgname}
pkgver=0.5.3
pkgrel=1
pkgdesc="Qiskit Experiments package for IBM qiskit framework"
arch=('any')
url="https://github.com/Qiskit/qiskit-experiments"
license=('Apache')
depends=(
    'python-lmfit'
    'python-matplotlib'
    'python-numpy'
    'python-qiskit-ibm-experiment'
    'python-qiskit-terra'
    'python-scipy'
    'python-uncertainties'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('d2ef5439410b239872e5fd92b3051c214c9b239a946c8a1c48791c2fa4cec92446953a1135de37ca27b1bacbb85d661645c29f1629be8e3c38cb0fda3dcf6652')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

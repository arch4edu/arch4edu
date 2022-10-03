# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-${_pkgname}
pkgver=0.4.0
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
    'python-qiskit-ibmq-provider'
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
b2sums=('1dea052f004f3df8d15d799cb8bdf5cfe8f0f7bc5acc22bf9788d7e2df2c734a6295f239af0c69792f0c6c6520ce9c3861ff2e23126fee38a34334aa19e3fec3')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

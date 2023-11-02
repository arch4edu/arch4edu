# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-${_pkgname}
pkgver=0.5.4
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
    'python-qiskit'
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
b2sums=('07663241aed0272646cc43529e0440dac5f80d7d0586d0067c12f7527829dd100a3e516af9368d9cc517f105d790380644b95cab9d5c98aeb7194fea3925f208')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

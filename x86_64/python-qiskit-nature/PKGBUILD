# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-nature
pkgname=python-${_pkgname}
pkgver=0.5.2
pkgrel=1
pkgdesc="Quantum Nature package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-nature"
license=('Apache')
depends=(
    'python-h5py'
    'python-numpy'
    'python-psutil'
    'python-qiskit-terra'
    'python-rustworkx'
    'python-scikit-learn'
    'python-scipy'
    'python-typing_extensions'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('ed5c0862422cd25517f13fae83acb524ef5fe951ecabe275aed676ff992c43ad1784b4c26224ead6762a44244f66b5250cdc14b25e762a2b4f657611d1d42572')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

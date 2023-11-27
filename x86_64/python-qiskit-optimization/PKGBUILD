# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-optimization
pkgname=python-${_pkgname}
pkgver=0.6.0
pkgrel=1
pkgdesc="Quantum Optimization package for IBM qiskit framework"
arch=('any')
url="https://github.com/qiskit-community/qiskit-optimization"
license=('Apache')
depends=(
    'python-docplex'
    'python-networkx'
    'python-numpy'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-scipy'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('d3d5641a1efd56f74502e04326ce135301e831ec660e09ab4f0fed708d1bdf606ae0d300e3c2b6c681182bd2f9e9b743f12377a72b6eced322bd4b45790700c7')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

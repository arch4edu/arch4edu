# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit
pkgname=python-${_pkgname}
pkgver=0.41.0
pkgrel=1
pkgdesc="An open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules"
arch=('any')
url="https://github.com/Qiskit/qiskit"
license=('Apache')
depends=(
    'python-qiskit-aer>=0.11.2'
    'python-qiskit-ibmq-provider>=0.20.0'
    'python-qiskit-terra>=0.23.1'
)
optdepends=(
    'python-qiskit-experiments: tools for building, running, and analysis of experiments on noisy quantum computers'
    'python-qiskit-finance: stock/securities problems, portfolio optimizations and finance experiments'
    'python-qiskit-machine-learning: sample datasets and quantum classification algorithms'
    'python-qiskit-nature: ground state energy computations, excited states and dipole moments of molecules'
    'python-qiskit-optimization: quantum optimization algorithms'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('1ae0d97d966e441520631521a36cacdd7ec38f02960697e74c2d932504ab1033a16c2bbefb1d42fe4e07fa3e17f4b116c22b017258da4d20473096c051da06d3')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

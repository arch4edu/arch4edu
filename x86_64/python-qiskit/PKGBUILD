# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-metapackage
pkgname=python-qiskit
pkgver=0.43.2
pkgrel=1
pkgdesc="An open-source SDK for working with quantum computers at the level of circuits, algorithms, and application modules"
arch=('any')
url="https://github.com/Qiskit/qiskit"
license=('Apache')
depends=(
    'python-qiskit-aer>=0.12.0'
    'python-qiskit-ibmq-provider>=0.20.2'
    'python-qiskit-terra>=0.24.0'
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
b2sums=('9692b69a4cb1d8350be4578313e85d7939970cf003975dad10cf2a70772b4e5826f94bdc2d50d23f0519380f96c7f49d13a5b2792411124b358e15e7e4dd0b2d')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

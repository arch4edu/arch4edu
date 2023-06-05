# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-metapackage
pkgname=python-qiskit
pkgver=0.43.1
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
b2sums=('5d161992ebf0b4900b1e466adad6d14d9fdd6bc12e215805363b948fb73761f5d1e977945a8b4db31dfdfa9675051288f7d3a0b63ccb3972fe44d25b567ed180')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

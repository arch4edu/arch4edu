# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-optimization
pkgname=python-${_pkgname}
pkgver=0.5.0
pkgrel=3
pkgdesc="Quantum Optimization package for IBM qiskit framework"
arch=('any')
url="https://github.com/Qiskit/qiskit-optimization"
license=('Apache')
depends=(
    'python-docplex'
    'python-networkx'
    'python-numpy'
    'python-qiskit'
    'python-scipy'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('271001d0293e05f145f5db20b09fef8dd90313eccf7b77d00d4bc249b7b4379dcdea817f19f80ec4bf4e022ef16a35d928022a8fd6a9d5ad21d5e9fcfdebbb0d')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

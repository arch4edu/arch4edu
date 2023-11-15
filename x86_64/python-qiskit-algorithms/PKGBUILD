# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-algorithms
pkgname=python-${_pkgname}
pkgver=0.2.1
pkgrel=2
pkgdesc="A library of quantum algorithms for Qiskit"
arch=('any')
url="https://github.com/qiskit-community/qiskit-algorithms"
license=('Apache')
depends=(
    'python-qiskit'
    'python-numpy'
    'python-scipy'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('f3508ceb96bd25806317eca0523209ee566296c5ee012ae4c0605784d257e5effccaf47f47a7333ad95b60b61bbf9d57ebe91e4ea7fb24208620ede1a92c0dfe')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

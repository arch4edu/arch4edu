# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-algorithms
pkgname=python-${_pkgname}
pkgver=0.2.2
pkgrel=1
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
b2sums=('54f3ffc77f4ceeb1e00c5d6a98b295c01bce0cc2a04902a5da9a8bd3bf39f4b1c6ddba6def8a685d5b7ff45efe2b37a12d4d9d96a88afd297b9ab771871028ca')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

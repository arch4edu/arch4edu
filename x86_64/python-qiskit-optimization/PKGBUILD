# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-optimization
pkgname=python-${_pkgname}
pkgver=0.4.0
pkgrel=1
pkgdesc="Quantum Optimization package for IBM qiskit framework"
arch=('any')
url="https://github.com/Qiskit/qiskit-optimization"
license=('Apache')
depends=(
    'python-docplex'
    'python-networkx'
    'python-numpy'
    'python-qiskit-terra'
    'python-scipy'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('856fca9031843fcb8a836c0612c4c488c195c4ee5dd011075327ec5221df3b053d68af35411e99d42d7a821e52737d7cdc2c6f2bdb63babb180f33ba04df8d88')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

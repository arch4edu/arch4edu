# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.6.1
pkgrel=2
pkgdesc="Quantum Machine Learning package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-machine-learning"
license=('Apache')
depends=(
    'python-dill'
    'python-fastdtw'
    'python-numpy'
    'python-psutil'
    'python-qiskit'
    'python-scikit-learn'
    'python-scipy'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('b81fba27891efcd6541404a664427cf21ffdd3a1d25889d9f37420ecdbf447d6d9d1564a7f9f138be51057be7683566c80cd44e65e936214222ba676d9707a32')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

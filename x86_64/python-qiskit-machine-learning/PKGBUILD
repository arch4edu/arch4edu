# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.6.0
pkgrel=1
pkgdesc="Quantum Machine Learning package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-machine-learning"
license=('Apache')
depends=(
    'python-dill'
    'python-fastdtw'
    'python-numpy'
    'python-psutil'
    'python-qiskit-terra'
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
b2sums=('267b934f691455ac5f30e18a372f40e531cd8b5b0cc46f0112ad1bd139cb199e905e42f2f5717a2f08ac423a9560d5664e31aa08a04bb24245951c6d7470e140')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

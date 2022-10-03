# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-machine-learning
pkgname=python-${_pkgname}
pkgver=0.4.0
pkgrel=3
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
checkdepends=(
    'python-qiskit-aer'
    'python-ddt'
    'python-pytest'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('0e2d56fe1375aba6ebc326818afe76fcf62fff44bfd0f413a2f8d0897fa104e77c70b73490e1fe2d539d9eae94b4da1363c848135e64a9a2b43859b7b31b6715')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    cd "${srcdir}/${_pkgname}-${pkgver}"
#    python -m pytest test/
#}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-experiments
pkgname=python-${_pkgname}
pkgver=0.6.0
pkgrel=1
pkgdesc="Qiskit Experiments package for IBM qiskit framework"
arch=('any')
url="https://github.com/Qiskit-Extensions/qiskit-experiments"
license=('Apache-2.0')
depends=(
    'python-lmfit'
    'python-matplotlib'
    'python-numpy'
    'python-pandas'
    'python-qiskit'
    'python-qiskit-ibm-experiment'
    'python-rustworkx'
    'python-scipy'
    'python-uncertainties'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
optdepends=(
    'python-cvxpy: for tomography'
    'python-scikit-learn: for discriminators'
    'python-qiskit-aer'
    'python-qiskit-dynamics: for the PulseBackend'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit-Extensions/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('ca70a579f7f22c2a1f83a0f5a499f36af29a7be8155ec9e2ce62b9b6b23f23d4bbd6c08af54251fbf13ff8c9fd1a0da1b7635b0bf88227f7d85af00e8f5b1f55')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

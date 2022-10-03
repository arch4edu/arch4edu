# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-finance
pkgname=python-${_pkgname}
pkgver=0.3.4
pkgrel=1
pkgdesc="Quantum Finance package for IBM qiskit framework"
arch=('any')
url="https://github.com/Qiskit/qiskit-finance"
license=('Apache')
depends=(
    'python-fastdtw'
    'python-numpy'
    'python-pandas'
    'python-psutil'
    'python-qiskit-optimization'
    'python-qiskit-terra'
    'python-quandl'
    'python-scikit-learn'
    'python-scipy'
    'python-yfinance'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('2666e60cc43dbc86b4ce6c4f6e7f2e971e66b5a5ef540026713dfecc65e3b4ed9432e1598c91f199e2da9964a4ad7a60c2836bb13d634a5461b0ac22b4f38488')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

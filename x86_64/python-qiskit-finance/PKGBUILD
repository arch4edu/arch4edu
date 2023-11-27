# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-finance
pkgname=python-${_pkgname}
pkgver=0.4.0
pkgrel=1
pkgdesc="Quantum Finance package for IBM qiskit framework"
arch=('any')
url="https://github.com/qiskit-community/qiskit-finance"
license=('Apache')
depends=(
    'python-certifi'
    'python-fastdtw'
    'python-nasdaq-data-link'
    'python-numpy'
    'python-pandas'
    'python-psutil'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-qiskit-optimization'
    'python-scipy'
    'python-urllib3'
    'python-yfinance'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/${pkgver}.tar.gz")
b2sums=('16f0335f9447bed5b99d860cdf38cbc296546091102f99f786fde2e0dfb3a95fe7e27886e6863f7c293b90cae53cb7a1f824b0b1139626ccf3abc071a96bdb5d')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

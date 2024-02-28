# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-algorithms
pkgname=python-${_pkgname}
pkgver=0.3.0
pkgrel=1
pkgdesc="A library of quantum algorithms for Qiskit"
arch=('any')
url="https://github.com/qiskit-community/qiskit-algorithms"
license=('Apache-2.0')
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
b2sums=('a0b7fd21a789e59dae47709cbcd294f7e7784f0f2007e30eb94dd88f09652a40cdf97f00965fd7828889f4675b647c7edafa9f5af5bab5950aae564ef286bb68')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

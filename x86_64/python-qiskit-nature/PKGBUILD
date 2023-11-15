# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-nature
pkgname=python-${_pkgname}
pkgver=0.7.0
pkgrel=1
pkgdesc="Quantum Nature package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/qiskit-community/qiskit-nature"
license=('Apache')
depends=(
    'python-h5py'
    'python-numpy'
    'python-psutil'
    'python-qiskit'
    'python-qiskit-algorithms'
    'python-rustworkx'
    'python-scipy'
    'python-typing_extensions'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/qiskit-community/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('822ec316840b404ac7c868498928845cc0fc25c7c1b56d42d93e99bb61520d27aee6dfc2cb2192c02756b32e437cb6c5ca781d8c0f973dd84f3a8493e0cd8279')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

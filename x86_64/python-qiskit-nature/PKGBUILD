# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=qiskit-nature
pkgname=python-${_pkgname}
pkgver=0.6.0
pkgrel=1
pkgdesc="Quantum Nature package for IBM qiskit framework"
arch=('x86_64')
url="https://github.com/Qiskit/qiskit-nature"
license=('Apache')
depends=(
    'python-h5py'
    'python-numpy'
    'python-psutil'
    'python-qiskit-terra'
    'python-rustworkx'
    'python-scikit-learn'
    'python-scipy'
    'python-typing_extensions'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/Qiskit/${_pkgname}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('02bc31bc14f7ac25a0fa8a962162bbc84723912b09a3b38db8ffcd7a7af73e4441724e1ae87d4345442aadc6118a7dd6467f20321e5f46956b30dacd21d56c42')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

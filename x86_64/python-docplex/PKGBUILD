# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.24.232
pkgrel=1
pkgdesc="The IBM Decision Optimization CPLEX Modeling for Python"
arch=('any')
url="https://pypi.org/project/docplex/"
license=('Apache')
depends=('python-six')
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
b2sums=('0c8e6404f933c74fef1b6b8a87c1a05ac4b8f9486aba3ad23fa3942ba7098257c8f6606d7624c8806dc903d6829c7295f8dbb9c8720057483a02ee00ef8466c8')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

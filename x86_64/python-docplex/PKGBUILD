# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.23.222
pkgrel=1
pkgdesc="The IBM Decision Optimization CPLEX Modeling for Python"
arch=('x86_64')
url="https://pypi.org/project/docplex/"
license=('Apache')
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz")
b2sums=('b2180eeebd1abd29bc9dd56ca6013d6ddeef53ae37240577afec96fab7f14e27f22ac7af11b3b8c13c0977252aa69bc6db7507c3162aa32c7d369f06f6f30b71')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

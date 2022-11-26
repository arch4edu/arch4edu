# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.24.231
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
b2sums=('2f005347980f5c2191088ecc3ec2fa615c834f6bbc05f395331bbf81b45a2baec58f709cbb12ad9a915f792b254576facad28d11d3fff73b729e94a9236705fb')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

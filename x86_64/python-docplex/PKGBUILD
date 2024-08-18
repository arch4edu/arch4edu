# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.28.240
pkgrel=1
pkgdesc="The IBM Decision Optimization CPLEX Modeling for Python"
arch=(any)
url=https://pypi.org/project/docplex/
license=(Apache-2.0)
depends=(python-six)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_pkgname-$pkgver.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/$_pkgname/$_pkgname-$pkgver.tar.gz)
b2sums=('9a353eec4583d9c591936de1e258acafc3afa27b58ac288164469118071a1e3499dc7bd84204ae6964d7b653e6d8a7454b7f7931f950230293f7237052dab406')

prepare() {
    sed -i -e 's/setuptools~=68.2.2/setuptools/' $_pkgname-$pkgver/pyproject.toml
}

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

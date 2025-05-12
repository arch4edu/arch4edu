# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.29.245
pkgrel=2
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
b2sums=('39caa6f5c2d1ba5f4250050e55704cd82d1b8319918cfe883f155110f19ab8157a053ab78f9252e6daaa635ed6b78553ad4c056c6ac4e619faba8bc182cbd6ec')

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

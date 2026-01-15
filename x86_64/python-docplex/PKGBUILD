# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.31.254
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
b2sums=('f8db6f0d8e5f86996146354500a743f2c2f1e3d39e2528231d5f9b66290468a6a87ddb05278c28395cea5663956d77cb485bbfb799b791a703f615141b95f63c')

prepare() {
    sed -i -e 's/setuptools~=78.1.1/setuptools/' $_pkgname-$pkgver/pyproject.toml
}

build() {
    cd $_pkgname-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

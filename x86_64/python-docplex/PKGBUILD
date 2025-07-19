# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.30.251
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
b2sums=('035fb3f18928b6dfb7f9eeee0fb73223ad93df0d78809b5e0878ce7b3c7d82d9ba0939084ed2134a3814ce05c3fb040b8a3a8f9e7f1f0a82dd099159efa0d663')

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

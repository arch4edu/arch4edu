# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=docplex
pkgname=python-docplex
pkgver=2.32.259
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
b2sums=('8241e7db2506cf458ff2af6ce245357d6082bf648799d96719b69b3b3e6c40ca10ebca00fbb0ca9473f5575175ecfbf36192d17e046818a0528606142c95d1d0')

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

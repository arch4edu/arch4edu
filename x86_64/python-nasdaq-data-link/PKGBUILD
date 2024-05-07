# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-nasdaq-data-link
_name=data-link-python
pkgver=1.0.4
pkgrel=3
pkgdesc="A Python library for Nasdaq Data Link's RESTful API"
arch=(any)
url=https://github.com/Nasdaq/data-link-python
license=(MIT)
depends=(
    python-dateutil
    python-inflection
    python-more-itertools
    python-numpy
    python-pandas
    python-requests
    python-six
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_name-$pkgver.tar.gz::https://github.com/Nasdaq/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('1eef49f0714463454236ef08d3672968cb30518d3fa6166011604e4af3d788861180ff1f82f36fc8ce322a199a62b59f9897a4098253ea25cf0401be37092006')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

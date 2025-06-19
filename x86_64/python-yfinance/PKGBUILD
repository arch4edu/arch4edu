# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.63
pkgrel=1
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-beautifulsoup4
    python-frozendict
    python-multitasking
    python-numpy
    python-pandas
    python-peewee
    python-platformdirs
    python-protobuf
    python-pytz
    python-requests
    python-requests-cache
    python-websockets
)
optdepends=(
    'python-pandas-datareader: to use pandas_datareader'
    'python-scipy: repair'
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_name-$pkgver.tar.gz::https://github.com/ranaroussi/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('6d300ef4e09540dbf4ac13baffaf9532aa1dda7bde87852d94f48bfc7c044e0cc01446bb7bf22fcc900abd617f70eccb4d07dafaac1ab2f9bef0e93580234864')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    # Remove weird entry point
    rm -rf "$pkgdir"/usr/bin
}

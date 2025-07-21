# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.65
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
b2sums=('fa46b805a636fc628e486918c6e6240ead09acfdaab55447538906548fd75acf183e24f0be8f5af040e0204482351f83433560f7f142cb6b1966ed4931d1cd7f')

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

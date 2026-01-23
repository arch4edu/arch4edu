# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.0
pkgrel=2
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-beautifulsoup4
    python-curl_cffi
    python-frozendict
    python-multitasking
    python-numpy
    python-pandas
    python-peewee
    python-platformdirs
    python-protobuf
    python-pytz
    python-requests
    python-websockets
)
optdepends=(
    'python-requests-cache: reduce requests'
    'python-requests-ratelimiter: limit requests'
    'python-scipy: repair'
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_name::git+https://github.com/ranaroussi/$_name.git#tag=$pkgver)
b2sums=('d37dbc57a69cd81d56da18a6d961064e8a9d9a9f9b4bfb34cd98d3fce51c1ec74b6c9afea2fe3bf9e5c61fd2b963e82c4a8989e740b36f339111516153b405c6')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    # Remove weird entry point
    rm -rf "$pkgdir"/usr/bin
}

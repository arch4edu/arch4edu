# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.3.0
pkgrel=1
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
b2sums=('72da3eab1c76fe043ef6d8194f2d1a834fe0497e5fd74d00f17118bd2ab0a4f3ec9dd759088746e583b423cb24988deaa505b0889accbc2242fda3beccc60386')

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

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.5.1
pkgrel=1
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-beautifulsoup4
    python-curl_cffi
    python-lxml
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
b2sums=('2804aec929449408e6558071dfae168cb0853da6653c116240123bfd4fd095a49541a1a5a0935bb27c677ac9b0f5edb245d9e81f7ad7932d354464b0a832317b')

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

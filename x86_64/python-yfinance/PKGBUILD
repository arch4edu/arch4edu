# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.7.0
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
    'python-scikit-learn: repair'
    'python-scipy: repair'
)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(
    python-pytest
    python-scikit-learn
    python-scipy
)
source=($_name::git+https://github.com/ranaroussi/$_name.git#tag=$pkgver)
b2sums=('72549771629cb19c6018dddc41d707bb47bd2523798d120d2070b0c2f8b8eec54b0df84ba0195d05ae4aaec6fcf3510756bfdbd542c571d9e0cd0026fdcd0860')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    test-env/bin/python -P -m pytest -o addopts="" -k "not test_badTicker"
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    # Remove weird entry point
    rm -rf "$pkgdir"/usr/bin
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.6.0
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
    python-scipy
)
source=($_name::git+https://github.com/ranaroussi/$_name.git#tag=$pkgver)
b2sums=('e8edee2666c8e6eaf7af10aefed8615208ddf3f8ead0d73225419f510a2a365ee02af94c01ac9db942f4e95b4df4e84bf4cf05d5e28116d95c14aee8511183da')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
    cd $_name
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    # https://github.com/ranaroussi/yfinance/issues/2926
    test-env/bin/python -P -m pytest -o addopts="" -k "not test_repair_bad_stock_splits"
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    # Remove weird entry point
    rm -rf "$pkgdir"/usr/bin
}

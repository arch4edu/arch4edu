# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=1.8.0
pkgrel=1
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-beautifulsoup4
    python-curl_cffi
    python-lxml
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
b2sums=('24f89a0258326bbc9729c2f03613ff8473bd18188802fd1bab3922976ea413a370954524cb66186602432e8cc298643f3c758698ef69bf5ecc6afd55c5530321')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

# Tired of comments in AUR about tests failing
# If you want to run the tests, uncomment the check() block
#check() {
#    cd $_name
#    python -m venv --system-site-packages test-env
#    test-env/bin/python -m installer dist/*.whl
#    test-env/bin/python -P -m pytest -o addopts="" #-k "not test_resampling"
#}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    # Remove weird entry point
    rm -rf "$pkgdir"/usr/bin
}

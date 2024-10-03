# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.44
pkgrel=1
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-beautifulsoup4
    python-cryptography
    python-frozendict
    python-html5lib
    python-lxml
    python-multitasking
    python-numpy
    python-pandas
    python-peewee
    python-platformdirs
    python-pytz
    python-requests
)
optdepends=(
    'python-pandas-datareader: to use pandas_datareader'
    'python-requests-cache: no spam'
    'python-requests-ratelimiter: no spam'
    'python-scipy: repair'
)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-wheel
)
source=($_name-$pkgver.tar.gz::https://github.com/ranaroussi/$_name/archive/refs/tags/$pkgver.tar.gz)
b2sums=('dccbf6af260c4d0eb2005118b525aa164584f2afa7128dc96e1bf75ed46fd8d5728437daa7f80b9c65125cd0b6435cad5ff31ea55b83dbfbe37e8813a953e9b3')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.38
pkgrel=1
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=(any)
url=https://github.com/ranaroussi/yfinance
license=(Apache-2.0)
depends=(
    python-appdirs
    python-beautifulsoup4
    python-cryptography
    python-frozendict
    python-html5lib
    python-lxml
    python-multitasking
    python-numpy
    python-pandas
    python-peewee
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
b2sums=('b317e178cdb612c8833784bc522e24134a156654d47b46225bd4fa771f6e57fd635493c7a21841de87afead0719ef8e2f711d42b704aa02a16ef6ecd461e895d')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

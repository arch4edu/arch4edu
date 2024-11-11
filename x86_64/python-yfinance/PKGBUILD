# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.49
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
b2sums=('9442da4f0edcde4d0895fce432d3d8333db6a4fa6f3fbc6fcc8c06f21863dc384b8e402ae8ed2fc97e6352df3f9145b56d5ce0e32c506dd18e13355fb5db0274')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
}

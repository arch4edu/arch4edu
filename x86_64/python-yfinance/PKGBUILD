# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.30
pkgrel=2
pkgdesc="Yahoo! Finance market data downloader (+faster Pandas Datareader)"
arch=('any')
url="https://github.com/ranaroussi/yfinance"
license=('Apache')
depends=(
    'python-appdirs'
    'python-beautifulsoup4'
    'python-cryptography'
    'python-frozendict'
    'python-html5lib'
    'python-lxml'
    'python-multitasking'
    'python-numpy'
    'python-pandas'
    'python-peewee'
    'python-pytz'
    'python-requests'
)
optdepends=('python-pandas-datareader: to use pandas_datareader')
makedepends=(
    'python-build'
    'python-installer'
    'python-wheel'
)
source=("${_name}-${pkgver}.tar.gz::https://github.com/ranaroussi/${_name}/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('f206713ac27cb0a9fae7238f407f061d221a0c41b0bb81bc8f7e36d8cb47c35f9974d1a088d28d57b5cfdf1080defd0f4ceac08aa77c65256218f78000da23d0')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

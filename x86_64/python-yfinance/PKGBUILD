# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.33
pkgrel=1
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
b2sums=('e56ad57584e5e1d9381c2a253485626b50df31eae325a9baf6e30ed5a61f14651844851e6ce3994da437bac79995dfc76a7133f2ad543c4c232cb0dc7fc10307')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

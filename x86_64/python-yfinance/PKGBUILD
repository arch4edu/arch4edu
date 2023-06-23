# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.21
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
b2sums=('f189674ab6370483afa9ab71778a2c818afb2f02e616c204841bfce7e29df777edb1865b3cff38f457f706f94b255a84c4fdd7fbfaa81c7ada071cf0f6cdbf10')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

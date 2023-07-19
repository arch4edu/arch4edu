# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.25
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
b2sums=('7b62f4874bbab3aca3736cefd07740715f04ff1b4daabe0ab0f2e44e1f682aecc37fb32ba3bea8d0720e14870383d5d836058cbac083dfeaea07649e3957ac33')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

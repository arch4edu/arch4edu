# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
pkgname=python-yfinance
_name=${pkgname#python-}
pkgver=0.2.23
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
b2sums=('dc76969354dc2fae3737ff423060cb9eac206b5616cab5ed3123cbeccd3f2dffa2943f5a25d2facd67e399ddf0e8520b856edad118a51b4003ac6f25b8b13a46')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

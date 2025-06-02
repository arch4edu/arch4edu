# Maintainer: Heavysink <winstonwu91@gmail.com>
pkgname=python-wrf
_pkgname='wrf-python'
pkgver=1.4.0
pkgrel=1
pkgdesc="A collection of diagnostic and interpolation routines for use with output from the Weather Research and Forecasting (WRF-ARW) Model."
url="https://wrf-python.readthedocs.io/en/latest/"
depends=('python' 'python-numpy')
makedepends=('python-build' 'python-installer' 'python-scikit-build-core' 'gcc-fortran')
provides=('wrf-python')
conflicts=('wrf-python')
license=('APACHE')
arch=('x86_64')
source=("https://github.com/NCAR/wrf-python/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('831600abbf4037c33a55c11ca9da5f8ee97b8b0276c205de8ab66cef85ff3589')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

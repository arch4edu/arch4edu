# Maintainer: Heavysink <winstonwu91@gmail.com>
pkgname=python-wrf
_pkgname='wrf-python'
pkgver=1.4.1
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
sha256sums=('975d7d128b15f5afea2245cab3a4929647c4295db3d440f366adf296afd9f766')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

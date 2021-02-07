# Maintainer: Heavysink <winstonwu91@gmail.com>
pkgname=python-wrf
_pkgname='wrf-python'
pkgver=1.3.2.5
pkgrel=1
pkgdesc="A collection of diagnostic and interpolation routines for use with output from the Weather Research and Forecasting (WRF-ARW) Model."
url="https://wrf-python.readthedocs.io/en/latest/"
depends=('python' 'python-numpy')
makedepends=('python-setuptools' 'python-pip' 'gcc-fortran')
provides=('wrf-python')
conflicts=('wrf-python')
license=('APACHE')
arch=('x86_64')
source=("https://github.com/NCAR/wrf-python/archive/$pkgver.tar.gz")
sha256sums=('8e54b2bca0fb095d9f94094cbe1463d74a351c5004930f4411fb963634589db4')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

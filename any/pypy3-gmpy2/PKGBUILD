# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy2
pkgname=pypy3-${_base}
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.3.1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/v${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('e3a1bb481e76baf1c365eaf34dd42cfd9ca49839d3d2f4c845ae462e8011f816174d73ced186f3eb24d928d3cf779defa7c2cd45da98842a8a57f886c741780b')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

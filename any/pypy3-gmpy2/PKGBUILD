# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy2
pkgname=pypy3-${_base}
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.3.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/v${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('a38c2b7e7e46d40381f0b38efc7f912833ac4b900014506db8d35385c5c1ca260dd6c5d96a30a5a7df296e7bdb1603a08d553640e5fc02d20c108d188e46aa15')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

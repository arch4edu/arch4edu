# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy
pkgname=pypy3-${_base}2
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.2.2a1
pkgrel=1
arch=(any)
url="https://github.com/aleaxit/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/${_base}2-${pkgver}.tar.gz)
sha512sums=('d99543409fdab962434e68c1bcdfbdf6f4cb9d5bb139e888592baa2c483ddb7cc5fc2fe8467debee68a980e1482f1fda06d98ae1411525cd6a310f82e014c95d')

build() {
  cd ${_base}-${_base}2-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${_base}2-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

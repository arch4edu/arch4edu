# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy2
pkgname=pypy3-${_base}
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.3.0b1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/v${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('90b1bb00524af58ebb69822d93d256b369b96a7fdf7d85e1bbe7fea1eb670d2c7a66695e795505068b5a0f84e4ba8442f0bf91ebd26b2b894de5a53a0efe615c')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

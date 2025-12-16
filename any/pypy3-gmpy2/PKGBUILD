# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=gmpy2
pkgname=pypy3-${_base}
pkgdesc="Interface to GMP, MPFR, and MPC"
pkgver=2.3.0a3
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(LGPL-3.0-or-later)
depends=(glibc gmp libmpc mpfr pypy3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${url}/archive/v${pkgver}/${_base}-${pkgver}.tar.gz)
sha512sums=('febbb519ae87d07bc5f89e9239f0274eca68cc87bb065c1941a50094f522873c92d5c0122c2ac8979835a50361272da0a7ccf703a7eff60668e535454b12d846')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 COPYING* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

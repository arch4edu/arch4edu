# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=mpmath
pkgname=pypy3-${_base}
pkgdesc="Python library for arbitrary-precision floating-point arithmetic"
pkgver=1.3.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-gmpy2)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('ec703e661323035e3c973fc2e52206e793f6182ed9897e5a483cb35a22421d7869df850cdd89fc1ef4e1bb28b17b4914447116dbeed136a687e582cce0bf9e42')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

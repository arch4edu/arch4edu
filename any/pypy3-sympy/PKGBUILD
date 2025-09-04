# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=sympy
pkgname=pypy3-${_base}
pkgdesc="Computer algebra system (CAS) in Python"
pkgver=1.14.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=(BSD)
depends=(pypy3-mpmath)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('c0b382634942fa9f282667d6573f63b505412ac2049096d84bc078b3956860c806f19044447e42991ce78de114afee22c1002fb956ea0383cb27800f2a940cd1')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

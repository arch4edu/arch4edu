# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pybind11
pkgname=pypy3-${_base}
pkgver=3.0.0
pkgrel=2
pkgdesc="A lightweight header-only library that exposes C++ types in Python and vice versa"
arch=(any)
url="https://${_base}.readthedocs.org"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(boost cmake eigen pypy3-build pypy3-installer pypy3-scikit-build-core)
source=(https://github.com/${_base::6}/${_base}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('a68a5eb3253db771308ed0922852207e6dc9a3089ad055ba3ccd36690f68b93cad98cc1a3ab822eb653153af2eeef10e6f6272b93314b2da1119e17f6c63337b')

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

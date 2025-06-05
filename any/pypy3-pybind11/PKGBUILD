# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pybind11
pkgname=pypy3-${_base}
pkgver=2.13.6
pkgrel=1
pkgdesc="A lightweight header-only library that exposes C++ types in Python and vice versa"
arch=(any)
url="https://${_base}.readthedocs.org"
license=(BSD-3-Clause)
depends=(pypy3)
makedepends=(cmake boost eigen pypy3-setuptools)
optdepends=('pypy3-setuptools: for python bindings')
source=(https://github.com/${_base::6}/${_base}/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz)
sha512sums=('497c25b33b09a9c42f67131ab82e35d689e8ce089dd7639be997305ff9a6d502447b79c824508c455d559e61f0186335b54dd2771d903a7c1621833930622d1a')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --skip-build --optimize='1'
  install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

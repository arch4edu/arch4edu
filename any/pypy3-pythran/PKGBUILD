# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pythran
pkgname=pypy3-${_base}
pkgdesc="Ahead of Time compiler for numeric kernels"
pkgver=0.18.1
pkgrel=1
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-ply pypy3-numpy pypy3-beniget xsimd boost)
makedepends=(pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('15650627b9396b49401067c3a7c161d1569f89f29a08243aa85659023e42ce028633915c51c8c5188a5599c201eb30aa2721d64ba766b2a252203469bc6e2ab1')

build() {
  cd ${_base}-${pkgver}
  pypy3 setup.py build
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 setup.py install --prefix=/opt/pypy3 --root="$pkgdir" --optimize=1 --skip-build
  rm -r "$pkgdir"/opt/pypy3/lib/py*/site-packages/pythran/{boost,xsimd} # Remove bundled boost and xsimd
  install -Dm644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}

# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=pythran
pkgname=pypy3-${_base}
pkgdesc="Ahead of Time compiler for numeric kernels"
pkgver=0.19.0
pkgrel=1
arch=(any)
url="https://github.com/serge-sans-paille/${_base}"
license=(BSD-3-Clause)
depends=(pypy3-ply pypy3-numpy pypy3-beniget xsimd boost)
makedepends=(pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz)
sha512sums=('e7238cdba1e6ab61f8268f52bc7224600ee5db9e54928d78c379ea61da4e00f121fcb03a9666ce0db1f3e3d9755695b6a9dd4f22f770bb554f5e438f04b4f37c')

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

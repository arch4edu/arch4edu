# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=pyparsing
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=3.3.1
pkgrel=1
pkgdesc="General parsing module for Python"
arch=(any)
url="https://github.com/${_base}/${_base}"
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
license=(MIT)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('897335233a642fefd05e729d86caeb6d1bb6b5873d6f4cf67dd922d0ec188efd9c051e2dad60df08f4876b61923078bb03f4cd93e835fe12e5c4e1ff6d591daa')

# Rename the following function to check() to enable checking
_check_pypy3-setuptools() {
  cd ${_base}-${pkgver}
  pypy3 unitTests.py
}

package_pypy3-pyparsing() {
  depends=(pypy3)

  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --no-isolation
  pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

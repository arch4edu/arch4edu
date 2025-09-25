# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=pyparsing
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=3.2.5
pkgrel=1
pkgdesc="General parsing module for Python"
arch=(any)
url="https://github.com/${_base}/${_base}"
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
license=(MIT)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('e9c4e4c7a7e324331ced2214b5a406c538209fedd8b56ffa2a28b44b497be0d4a03b705e9ce9a449e8f126a8fa555e8c1572894b09dda0eda4e3da156ba7e3ff')

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

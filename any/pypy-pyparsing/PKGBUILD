# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=pyparsing
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=3.3.0
pkgrel=1
pkgdesc="General parsing module for Python"
arch=(any)
url="https://github.com/${_base}/${_base}"
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
license=(MIT)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('14251bce003aad2f678377d7b372e093cc01b14674f831832165ec56a449a642ba6ce129e0ac7f9bf372a1ee14270f72e709713278040563d9076a59f0251aa0')

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

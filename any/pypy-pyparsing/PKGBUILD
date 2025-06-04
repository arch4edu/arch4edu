# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=pyparsing
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=3.2.3
pkgrel=1
pkgdesc="General parsing module for Python"
arch=(any)
url="https://github.com/${_base}/${_base}"
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
license=(MIT)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('ef01403a158f15215b3be7f7c4aad2ceb6020d578dac68351b732df3447c685aa478d23ab645d554070ad2aec14ee565a0407f428b91f398e4429c0e53eb4a6d')

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

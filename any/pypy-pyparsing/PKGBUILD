# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=pyparsing
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=3.2.4
pkgrel=1
pkgdesc="General parsing module for Python"
arch=(any)
url="https://github.com/${_base}/${_base}"
makedepends=(pypy3-build pypy3-installer pypy3-flit-core)
license=(MIT)
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('a7cd44fb37aba3b0fb92bf8f64ba192136c892c6bf41f9a5ebda694c2263a121b0123406e4e3e8ea203b01b0185e05a12f8937fc7a4f494d9be7ddaea43faf65')

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

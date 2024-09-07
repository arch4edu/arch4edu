# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Daniel Milde <daniel@milde.cz>
_base=packaging
pkgbase=pypy-${_base}
pkgname=pypy3-packaging
pkgver=21.3
pkgrel=2
pkgdesc="Core utilities for Python packages"
arch=(any)
url="https://github.com/pypa/${_base}"
license=(Apache-2.0 BSD-2-Clause)
makedepends=(pypy3-setuptools70) # pypa/setuptools/issues/4483
source=(https://pypi.org/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('2e3aa276a4229ac7dc0654d586799473ced9761a83aa4159660d37ae1a2a8f30e987248dd0e260e2834106b589f259a57ce9936eef0dcc3c430a99ac6b663e05')

package_pypy3-packaging() {
  depends=(pypy3-pyparsing)

  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

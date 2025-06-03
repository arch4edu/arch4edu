# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributer: Daniel Milde <daniel@milde.cz>
# Contributer: Markus Kitsinger (SwooshyCueb) <root@swooshalicio.us>
# Contributer: Jelle van der Waa <jelle@vdwaa.nl>
# Contributer: Allan McRae <allan@archlinux.org>
_base=six
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=1.17.0
pkgrel=1
pkgdesc="Python 2 and 3 compatibility utilities (build for pypy)"
arch=(any)
url="https://pypi.python.org/pypi/${_base}"
license=(MIT)
makedepends=(pypy3-setuptools)
source=(https://pypi.io/packages/source/${_base::1}/${_base}/${_base}-${pkgver}.tar.gz)
sha512sums=('fcfa58b03877ac3ac00a4f85b5fea4fecb2a010244451aa95013637a0aa21529f3dcfe25c0a07c72da46da1fa12bc0c16b6c641c40c6ab2133e5b5cbb5a71e4b')

package_pypy3-six() {
  depends=(pypy3)
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

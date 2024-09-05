# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributer: Daniel Milde <daniel@milde.cz>
# Contributer: Markus Kitsinger (SwooshyCueb) <root@swooshalicio.us>
# Contributer: Jelle van der Waa <jelle@vdwaa.nl>
# Contributer: Allan McRae <allan@archlinux.org>
_base=six
pkgbase=pypy-${_base}
pkgname=pypy3-${_base}
pkgver=1.16.0
pkgrel=1
pkgdesc="Python 2 and 3 compatibility utilities (build for pypy)"
arch=(any)
url="https://pypi.python.org/pypi/${_base}"
license=(MIT)
makedepends=(pypy3-setuptools)
source=("https://pypi.io/packages/source/s/six/six-$pkgver.tar.gz")
sha512sums=('076fe31c8f03b0b52ff44346759c7dc8317da0972403b84dfe5898179f55acdba6c78827e0f8a53ff20afe8b76432c6fe0d655a75c24259d9acbaa4d9e8015c0')

package_pypy3-six() {
  depends=(pypy3)
  cd ${_base}-${pkgver}
  pypy3 setup.py install --prefix=/opt/pypy3 --root="${pkgdir}" --optimize=1
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

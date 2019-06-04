# Maintainer: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=python2-sortedcontainers
_pkgname=python-sortedcontainers
pkgver=2.1.0
pkgrel=1
pkgdesc='Library providing sorted container types for Python.'
arch=(any)
url=https://github.com/grantjenks/python-sortedcontainers
license=('custom:Apache2')
depends=(python2)
makedepends=(python2-setuptools)
source=(https://github.com/grantjenks/${_pkgname}/archive/v${pkgver}.tar.gz)
md5sums=('1aa2d4cef402341fdeea75bc51311e59')

build() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python2 setup.py build
}

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python2 setup.py install --root=${pkgdir} --optimize=1
  install -d -m 755 ${pkgdir}/usr/share/licenses/${pkgname}
  install -D -m 644 LICENSE ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}

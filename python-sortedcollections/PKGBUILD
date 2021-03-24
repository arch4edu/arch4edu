# Maintainer: Sam Whited <sam@samwhited.com>
# Contributor: Amos Onn <amosonn at gmail dot com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr>

pkgname=python-sortedcollections
_name=${pkgname#python-}
pkgver=2.1.0
pkgrel=1
pkgdesc="A python library for sorted collections."
arch=('any')
url="http://www.grantjenks.com/docs/sortedcollections/"
license=(Apache)
depends=('python-sortedcontainers>=2.0.0')
makedepends=('python-setuptools')
source=("https://codeload.github.com/grantjenks/$pkgname/tar.gz/refs/tags/v$pkgver")
sha256sums=("4a70235d04737268feaed645e11c4aa25d165f0c69114f92d71e84ecb3e99ccf")

package_python-sortedcollections() {
  cd $pkgname-$pkgver
  python setup.py install --root="$pkgdir"
}

# vim: ts=2 sw=2 et:

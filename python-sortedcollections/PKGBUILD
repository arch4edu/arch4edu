# Maintainer: Sam Whited <sam@samwhited.com>
# Contributor: Amos Onn <amosonn at gmail dot com>
# Contributor: Emmanuel Gil Peyrot <linkmauve@linkmauve.fr>

pkgname=python-sortedcollections
_name=${pkgname#python-}
pkgver=1.1.2
pkgrel=2
pkgdesc="A python library for sorted collections."
arch=('any')
url="http://www.grantjenks.com/docs/sortedcollections/"
license=(Apache)
depends=('python-sortedcontainers>=2.0.0')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('b93e0decbd7f8f19e40c320709e70e4845b6c8b3a0e96c3c4f707b4b93e1d38a')

package_python-sortedcollections() {
  cd $_name-$pkgver
  python setup.py install --root="$pkgdir"
}

# vim: ts=2 sw=2 et:

# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=python-configshell-fb
_pkgname=configshell-fb
pkgver=1.1.30
pkgrel=1
pkgdesc="python framework for building simple CLI applications (free branch)"
arch=('any')
url="https://github.com/open-iscsi/configshell-fb"
license=('Apache')
options=()
depends=('python-pyparsing' 'python-urwid')
makedepends=('python-setuptools')
provides=('python-configshell')
conflicts=('python-configshell')
source=(https://github.com/open-iscsi/configshell-fb/archive/v${pkgver}.tar.gz)
sha512sums=('b3189130ac047fe28ea987391591b7886f7234864d455a8423d1d65b02a514511e2a32dce1429a6b71cedbc0b7cb6e6e10f29d240b746d222c285f0baa6b46b0')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:

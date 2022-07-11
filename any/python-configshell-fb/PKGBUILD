# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=python-configshell-fb
_pkgname=configshell-fb
pkgver=1.1.29
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
sha512sums=('1b5f573506317119d2420e415abbb856692caa65a7f407f741300eec302d1b442e29d2691f6a192b202b2a5731a7a179d1b03f6cd27780876194d97e4df5f7d0')

package() {
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:

# Contributor: Johannes Dewender  arch at JonnyJD dot net
pkgname=('python-configshell-fb' 'python2-configshell-fb')
_pkgname=configshell-fb
pkgver=1.1.26
pkgrel=1
pkgdesc="python framework for building simple CLI applications (free branch)"
arch=('any')
url="https://github.com/open-iscsi/configshell-fb"
license=('Apache')
options=()
makedepends=('python-setuptools' 'python2-setuptools')
source=(https://github.com/open-iscsi/configshell-fb/archive/v${pkgver}.tar.gz)
sha512sums=('25e5b4ee812a51c99eed4d039ac8bab883218a674ff27f9eee4604d133b592574f4829ead9cb1aba4d2aca873f5414ad4ca55979c6d4eadaa9a802b1d563494d')

package_python-configshell-fb() {
  depends=('python-pyparsing' 'python-urwid')
  provides=('python-configshell')
  conflicts=('python-configshell')
  cd "$srcdir/$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

package_python2-configshell-fb() {
  depends=('python2-pyparsing' 'python2-urwid')
  provides=('python2-configshell')
  conflicts=('python2-configshell')
  cd "$srcdir/$_pkgname-$pkgver"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:

# Maintainer: Bruno Galeotti <bgaleotti at gmail dot com>

pkgname=python2-tabulate
pkgver=0.8.2
pkgrel=1
pkgdesc="Pretty-print tabular data in Python."
arch=(any)
url="https://bitbucket.org/astanin/python-tabulate"
depends=('python2' 'python2-psutil')
source=("https://pypi.python.org/packages/12/c2/11d6845db5edf1295bc08b2f488cf5937806586afe42936c3f34c097ebdc/tabulate-0.8.2.tar.gz")
sha256sums=('e4ca13f26d0a6be2a2915428dc21e732f1e44dad7f76d7030b2ef1ec251cf7f2')
license=('MIT')

build() {
  cd "$srcdir/tabulate-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/tabulate-$pkgver"
  python2 setup.py install --root=$pkgdir --optimize=1
  find "$pkgdir" -name '*.py' -print0 |xargs -0 \
    sed -i -e 's,^#!/usr/bin/env python$,#!/usr/bin/env python2,' \
    -e 's,^#!/usr/bin/python$,#!/usr/bin/python2,'
}

# vim:set ts=2 sw=2 et:

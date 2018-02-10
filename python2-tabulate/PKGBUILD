# Maintainer: Bruno Galeotti <bgaleotti at gmail dot com>

pkgname=python2-tabulate
pkgver=0.8.1
pkgrel=1
pkgdesc="Pretty-print tabular data in Python."
arch=(any)
url="https://bitbucket.org/astanin/python-tabulate"
depends=('python2' 'python2-psutil')
#source=("https://pypi.python.org/packages/b6/88/0bd3eff61b663bd25ae824d60de5fdc441a872f1c8988bb5a057a7432a44/tabulate-0.8.1.tar.gz")
source=("https://bitbucket.org/astanin/python-tabulate/get/v$pkgver.tar.gz")
sha256sums=('00c2569b2795dcf19ef45767444fa69e2cd2a040687800d81512e3acc9558d08')
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

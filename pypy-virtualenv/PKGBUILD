# $Id: PKGBUILD 179889 2013-03-11 02:36:11Z dan $
# Contributor: Michael Beasley <youvegotmoxie@gmail.com
# Contributor: Daniele Paolella <dp@mcrservice.it>

pkgname=('pypy-virtualenv' 'pypy3-virtualenv')
pkgver=15.1.0
pkgrel=1
pkgdesc="Virtual Python Environment builder for pypy"
url="https://virtualenv.pypa.io/"
arch=('any')
license=('MIT')
makedepends=('pypy' 'pypy3')
source=("https://pypi.io/packages/source/v/virtualenv/virtualenv-$pkgver.tar.gz")
md5sums=('44e19f4134906fe2d75124427dc9b716')
sha256sums=('02f8102c2436bb03b3ee6dede1919d1dac8a427541652e5ec95171ec8adbc93a')

package_pypy-virtualenv() {
  depends=('pypy')

  cd "$srcdir/virtualenv-$pkgver"

  # should report this upstream as still not fixed...
  sed -i "s|#!/usr/bin/env python$|#!/usr/bin/env pypy|" virtualenv.py

  LANG='en_US.UTF-8' pypy setup.py build
  LANG='en_US.UTF-8' pypy setup.py install --root="$pkgdir"

  mkdir -p "${pkgdir}"/usr/bin

  # link to a version with 2 suffix as well
  ln "$pkgdir/opt/pypy/bin/virtualenv" "$pkgdir/usr/bin/virtualenv-pypy2"
  ln "$pkgdir/opt/pypy/bin/virtualenv" "$pkgdir/usr/bin/virtualenv-pypy-2.7"
  ln "$pkgdir/usr/bin/virtualenv-pypy2" "$pkgdir/usr/bin/virtualenv-pypy"

  install -D -m644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

package_pypy3-virtualenv() {
  depends=('pypy3')

  cd "$srcdir/virtualenv-$pkgver"

  # should report this upstream as still not fixed...
  sed -i "s|#!/usr/bin/env python$|#!/usr/bin/env pypy3|" virtualenv.py

  LANG='en_US.UTF-8' pypy3 setup.py build
  LANG='en_US.UTF-8' pypy3 setup.py install --root="$pkgdir"

  mkdir -p "${pkgdir}"/usr/bin

  # link to a version with 2 suffix as well
  ln "$pkgdir/opt/pypy3/bin/virtualenv" "$pkgdir/usr/bin/virtualenv-pypy3"
  ln "$pkgdir/opt/pypy3/bin/virtualenv" "$pkgdir/usr/bin/virtualenv-pypy-3.3"

  install -D -m644 LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

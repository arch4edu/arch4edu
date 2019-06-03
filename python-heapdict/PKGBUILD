# Maintainer: Amos Onn <amosonn at gmail dot com>
pkgbase=python-heapdict
pkgname=('python-heapdict' 'python2-heapdict')
_pkgname=heapdict
pkgver=1.0.0
pkgrel=2
pkgdesc="A python library for a heap with decrease- and increase-key operations."
arch=('any')
url="http://stutzbachenterprises.com"
license=('BSD-3-clause')
source=(https://codeload.github.com/DanielStutzbach/heapdict/tar.gz/v$pkgver)
sha256sums=('4c8e581f1651ca78da35820fc80b0d50fc060032517f2c7efd9169e204db3793')

prepare() {
  cp -a $_pkgname-$pkgver{,-py2}
}

package_python-heapdict() {
  depends=('python')
  cd $srcdir/$_pkgname-$pkgver
  python setup.py install --root=$pkgdir || return 1
  install -d $pkgdir/usr/share/licenses/$pkgname
  install LICENSE $pkgdir/usr/share/licenses/$pkgname/COPYING
}

package_python2-heapdict() {
  depends=('python2')
  cd $srcdir/$_pkgname-$pkgver-py2
  python2 setup.py install --root=$pkgdir || return 1
  install -d $pkgdir/usr/share/licenses/$pkgname
  install LICENSE $pkgdir/usr/share/licenses/$pkgname/COPYING
}
